import os
import pandas as pd

pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
ans_path = father_path+'\\Data\\Prediction'
ans_files = os.listdir(ans_path)
file_csv = list(filter(lambda x: x[-4:] == '.csv', ans_files))


for file in file_csv:
    df_ans = pd.read_csv(ans_path+'\\'+file, header=None, names=['Level','Prediction'])
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(df_ans)):
        if abs(df_ans.iat[i, 0].astype(float) - df_ans.iat[i, 1].astype(float)) <= 0.5:
            cnt1 = cnt1 + 1
        if abs(df_ans.iat[i, 0].astype(float) - df_ans.iat[i, 1].astype(float)) <= 1:
            cnt2 = cnt2 + 1
        if abs(df_ans.iat[i, 0].astype(float) - df_ans.iat[i, 1].astype(float)) <= 1.5:
            cnt3 = cnt3 + 1
    print('Verify ' + ans_path + '\\' + file + ' AccuracyRate1 = ' + str(cnt1 / len(df_ans)))
    print('Verify ' + ans_path + '\\' + file + ' AccuracyRate2 = ' + str(cnt2 / len(df_ans)))
    print('Verify ' + ans_path + '\\' + file + ' AccuracyRate3 = ' + str(cnt3 / len(df_ans)))
    print('--------------------------------------------------------------------------------')
print("Verify successfully!")
