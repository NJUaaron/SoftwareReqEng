import os
import pandas as pd

pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
read_path = father_path+'\\Data\\Class'
save_path = father_path+'\\Data\\NewRaw'

files = os.listdir(read_path)
files_csv = list(filter(lambda x: x[-4:] == '.csv', files))

fp_0 = open(save_path+'\\newraw0.csv', 'w+', encoding='utf8')
fp_1 = open(save_path+'\\newraw1.csv', 'w+', encoding='utf8')
fp_2 = open(save_path+'\\newraw2.csv', 'w+', encoding='utf8')
fp_3 = open(save_path+'\\newraw3.csv', 'w+', encoding='utf8')
fp_4 = open(save_path+'\\newraw4.csv', 'w+', encoding='utf8')
fp_5 = open(save_path+'\\newraw5.csv', 'w+', encoding='utf8')
fp_6 = open(save_path+'\\newraw6.csv', 'w+', encoding='utf8')
fp_7 = open(save_path+'\\newraw7.csv', 'w+', encoding='utf8')
fp_8 = open(save_path+'\\newraw8.csv', 'w+', encoding='utf8')
fp_9 = open(save_path+'\\newraw9.csv', 'w+', encoding='utf8')

for file in files_csv:
    df = pd.read_csv(read_path+'\\'+file, header=None, names=['No','Title','Content','Level'])
    for i in range(len(df)):
            if i % 10 == 0:
                fp_0.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 1:
                fp_1.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 2:
                fp_2.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 3:
                fp_3.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 4:
                fp_4.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 5:
                fp_5.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 6:
                fp_6.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 7:
                fp_7.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 8:
                fp_8.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
            elif i % 10 == 9:
                fp_9.write( df.iat[i, 0].astype(str) + ',' + df.iat[i, 1] + ',' + df.iat[i, 2] + ',' + df.iat[i, 3].astype(str) + '\n')
    print('Average ' + file + ' DONE')

fp_0.close()
fp_1.close()
fp_2.close()
fp_3.close()
fp_4.close()
fp_5.close()
fp_6.close()
fp_7.close()
fp_8.close()
fp_9.close()
