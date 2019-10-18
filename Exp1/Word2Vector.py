from gensim.models import word2vec
import numpy as np


def readCSV(filename):
    file = open('./' + filename, encoding='utf8')
    raw_doc = file.read()
    file.close()
    List = raw_doc.split('\n')
    for i in range(len(List)):
        List[i] = List[i].split(',')  # 按逗號分割
        # print(L[i])
    return List


sentence_list = readCSV(r"word.csv")
vecSize = 100
model = word2vec.Word2Vec(sentence_list, hs=0, sg=1, min_count=0, window=5, size=vecSize)
print('Model Build Complete! Model shape : ', model.wv.syn0.shape)
# for i in range(model.wv.syn0.shape[0]):
#     print(model.wv.index2word[i])
# print(model['Visual Studio Code'])

""" 生成句向量 """
senVec_list = []  # sentence vector list
# wordVec_amount = model.wv.syn0.shape[0]
for i in range(len(sentence_list)):
    senVec = np.array([0] * vecSize)
    for word in sentence_list[i]:
        wordVec = model[word]  # Deprecated method!!
        senVec = senVec + wordVec
    senVec = senVec / len(sentence_list[i])  # 句向量为句中所有词向取平均数
    # print(senVec)
    senVec_list.append(list(senVec))

    # for j in range(len(senVec_list)):
    #     print(senVec_list[j])
    # print()

print('Word2Vec Complete!')
# print(senVec_list)

''' Save to CSV '''
f = open('./vec.csv', 'w')
senVec_num = 1
for senVec in senVec_list:
    f.write(str(senVec_num))
    f.write(',')
    for i in range(len(senVec)):
        if i != 0:
            f.write(',')
        f.write(str(senVec[i]))
    f.write("\n")
    senVec_num = senVec_num+1
f.close()
print('vec.csv save complete !')
