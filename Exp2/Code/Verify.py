import os

import nltk
import pandas as pd

pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
raw_path = father_path+'\\Data\\Raw'
ans_path = father_path+'\\Data\\Prediction'
raw_files = os.listdir(raw_path)
ans_files = os.listdir(ans_path)
file_csv = list(filter(lambda x: x[-4:] == '.csv', raw_files))


for file in file_csv:
    df_raw = pd.read_csv(raw_path+'\\'+file, header=None, names=['No','Title','Content','Level'])
    df_ans = pd.read_csv(ans_path+'\\'+file, header=None, names=['No','Ans'])
    cnt1 = 0
    cnt2 = 0
    for i in range(len(df_raw)):
        if df_raw.iat[i, 3].astype(int) == df_ans.iat[i, 1].astype(int):
            cnt1 = cnt1 + 1
        if abs(df_raw.iat[i, 3].astype(int) - df_ans.iat[i, 1].astype(int)) <= 1:
            cnt2 = cnt2 + 1
    print('Verify ' + ans_path + '\\' + file + ' AccuracyRate1 = ' + str(cnt1 / len(df_raw)))
    print('Verify ' + ans_path + '\\' + file + ' AccuracyRate2 = ' + str(cnt2 / len(df_raw)))
print("Verify successfully!")
