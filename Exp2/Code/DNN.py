#单个文件进行1次5-fold，保存5次的预测结果
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def readMetrix(filePath):
    vecList = []
    with open(filePath, 'r') as f:
        for line in f:
            row = []
            for d in line.split(','):
                row.append(float(d))
            vecList.append(row)
    return vecList

def readLabel(filePath):
    yList = []
    with open(filePath, 'r') as f:
        for line in f:
            row = line.split(',')
            yList.append(float(row[len(row)-1]))
    return yList

def readData(father_path, f):
    metrix_read_path = father_path+'\\Data\\Vec'
    label_read_path = father_path+'\\Data\\Raw'

    files1 = os.listdir(metrix_read_path)
    files_csv1 = list(filter(lambda x: x[-4:] == '.csv', files1))
    files2 = os.listdir(label_read_path)
    files_csv2 = list(filter(lambda x: x[-4:] == '.csv', files2))
    file_num = len(files_csv1)
    x_train = []
    x_test = []
    y_train = []
    y_test = []
    for index in range(file_num):
        metrix_path = metrix_read_path+'\\'+files_csv1[index]
        label_path = label_read_path+'\\'+files_csv2[index]
        if index == f:
            x_test = readMetrix(metrix_path)
            y_test = readLabel(label_path)
        else:
            x_train += readMetrix(metrix_path)
            y_train += readLabel(label_path)
    print("Wordvec Read Complete!")
    return x_train, x_test, y_train, y_test


if __name__ == '__main__':
    pwd = os.getcwd()
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    save_path = father_path+'\\Data\\Prediction'

    #10-fold
    for f in range(10):
        #read data
        x_train, x_test, y_train, y_test = readData(father_path, f)

        '''
        print(x_train)
        print(x_test)
        print(y_train)
        print(y_test)
        '''

        def normalize_cols(m):
            col_max = m.max(axis=0)
            col_min = m.min(axis=0)
            return (m - col_min) / (col_max - col_min)


        x_train = np.nan_to_num(normalize_cols(np.array(x_train)))
        x_test = np.nan_to_num(normalize_cols(np.array(x_test)))
        y_train = [i/5.0 for i in y_train]
        y_test = [i/5.0 for i in y_test]

        sess = tf.Session()

        #DNN parameters
        metrix_num = 50
        batch_size = 50
        hidden_layer_nodes1 = 30
        hidden_layer_nodes2 = 15
        step_length = 0.0002
        seed = tf.set_random_seed(2019)

        np.random.seed(seed)

        #nerual network model
        x_data = tf.placeholder(shape=[None, metrix_num], dtype=tf.float32)
        y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
        A1 = tf.Variable(tf.random_normal(shape=[metrix_num, hidden_layer_nodes1]))
        b1 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes1]))  #hidden layer1
        A2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes1, hidden_layer_nodes2]))
        b2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes2]))  #hidden layer2
        A3 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes2, 1]))
        b3 = tf.Variable(tf.random_normal(shape=[1]))                   #output layer

        hiddden_output1 = tf.add(tf.matmul(x_data, A1), b1)
        hiddden_output2 = tf.add(tf.matmul(hiddden_output1, A2), b2)
        final_output = tf.nn.sigmoid(tf.add(tf.matmul(hiddden_output2, A3), b3))

        #use cross entropy as loss
        loss = -tf.reduce_mean(y_target * tf.log(final_output + 1e-10) + (1 - y_target) * tf.log(1 - final_output + 1e-10))

        my_opt = tf.train.AdamOptimizer(step_length)
        train_step = my_opt.minimize(loss)

        sess.run(tf.global_variables_initializer())

        #Train
        loss_vec = []
        test_loss = []
        for i in range(20000):
            #First we select a random set of indices for the batch
            rand_index = np.random.choice(len(x_train), size=batch_size)

            #Then we select the training valuses
            rand_x = np.array(x_train)[rand_index]
            rand_y = np.transpose([ np.array(y_train)[rand_index]])
            #now we run the training step
            sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
            #We save the training loss
            temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
            loss_vec.append(np.sqrt(abs(temp_loss)))
            #Finally, we run the test-set loss and save it
            test_temp_loss = sess.run(loss, feed_dict={x_data: x_test, y_target: np.transpose([y_test])})
            test_loss.append(np.sqrt(abs(test_temp_loss)))
            if i%100 == 0:
                print('range'+str(i)+' train loss='+str(temp_loss)+' test loss='+str(test_temp_loss))

        #Predict
        test_output = sess.run(final_output, feed_dict={x_data: x_test, y_target: np.transpose([y_test])})
        test_output_vec = np.transpose(test_output)[0]
        result_save = open(save_path+'\\'+str(f)+'.csv', 'w')
        result_save.write('level,prediction\n')
        for i in range(len(test_output_vec)):
            result_save.write(str(y_test[i]) + ',' + str(test_output_vec[i]) + '\n')
        result_save.close()
        print('result saved.')

        #Accuracy
        acc_1 = 0       #<=0.5
        acc_2 = 0       #<=1
        acc_3 = 0       #<=1.5
        for i in range(len(y_test)):
            error = abs(y_test[i]-test_output_vec[i])
            if error < 0.1:
                acc_1 += 1
            if error < 0.2:
                acc_2 += 1
            if error < 0.3:
                acc_3 += 1
        print('accuracy1 = '+str(acc_1/len(y_test)))
        print('accuracy2 = '+str(acc_2/len(y_test)))
        print('accuracy3 = '+str(acc_3/len(y_test)))

    # plt.plot(loss_vec, 'k-', label='Train Loss')
    # plt.plot(test_loss, 'r--', label='Test Loss')
    # plt.title('Loss (CE) per Generation')
    # plt.xlabel('Generation')
    # plt.ylabel('Loss')
    # plt.legend(loc='upper right')
    # plt.show()


    print('Output completed')









