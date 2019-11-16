import os
import pandas as pd

pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
read_path = father_path+'\\Data\\Raw'
save_path = father_path+'\\Data\\Class'

files = os.listdir(read_path)
files_csv = list(filter(lambda x: x[-4:] == '.csv', files))

fp_1 = open(save_path+'\\level_1.csv', 'w+', encoding='utf8')
fp_2 = open(save_path+'\\level_2.csv', 'w+', encoding='utf8')
fp_3 = open(save_path+'\\level_3.csv', 'w+', encoding='utf8')
fp_4 = open(save_path+'\\level_4.csv', 'w+', encoding='utf8')
fp_5 = open(save_path+'\\level_5.csv', 'w+', encoding='utf8')

for file in files_csv:
    if file == 'raw10.csv':
        df = pd.read_csv(read_path+'\\'+file, header=None, names=['No','Title','Content','Level'])
        for i in range(len(df)):
            if df.iat[i, 3].astype(int) == 1:
                fp_1.write( df.iat[i, 0].astype(str) + ',' +
                            df.iat[i, 1] + ',' + df.iat[i, 2] + ',' +
                            df.iat[i, 3].astype(str) + '\n')
            elif df.iat[i, 3].astype(int) == 2:
                fp_2.write( df.iat[i, 0].astype(str) + ',' +
                            df.iat[i, 1] + ',' + df.iat[i, 2] + ',' +
                            df.iat[i, 3].astype(str) + '\n')
            elif df.iat[i, 3].astype(int) == 4:
                fp_4.write( df.iat[i, 0].astype(str) + ',' +
                            df.iat[i, 1] + ',' + df.iat[i, 2] + ',' +
                            df.iat[i, 3].astype(str) + '\n')
            elif df.iat[i, 3].astype(int) == 5:
                fp_5.write( df.iat[i, 0].astype(str) + ',' +
                            df.iat[i, 1] + ',' + df.iat[i, 2] + ',' +
                            df.iat[i, 3].astype(str) + '\n')
    else:
        df = pd.read_csv(read_path + '\\' + file, header=None, names=['No', 'Title', 'Content', 'Level'])
        for i in range(len(df)):
            if df.iat[i, 3].astype(int) == 3:
                fp_3.write(df.iat[i, 0].astype(str) + ',' +
                           df.iat[i, 1] + ',' + df.iat[i, 2] + ',' +
                           df.iat[i, 3].astype(str) + '\n')
    print('Classify ' + file + ' DONE')

fp_1.close()
fp_2.close()
fp_3.close()
fp_4.close()
fp_5.close()
