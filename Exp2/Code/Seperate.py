import os
import nltk
import pandas as pd
from nltk.corpus import stopwords

pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
read_path = father_path+'\\Data\\Raw'
save_path = father_path+'\\Data\\Word'

stopWords = set(stopwords.words('english'))

files = os.listdir(read_path)
files_csv = list(filter(lambda x: x[-4:] == '.csv', files))

for file in files_csv:
    df = pd.read_csv(read_path+'\\'+file, header=None, names=['No','Title','Content','Level'])
    fp = open(save_path+'\\'+file, 'w+', encoding='utf8')
    for i in range(len(df)):
        if i != 0:
            fp.write('\n')
        fp.write(df.iat[i, 0].astype(str) + ',')
        text = df.iat[i, 1] + ' '+ df.iat[i, 2]
        disease_List = nltk.word_tokenize(text)
        filtered = []
        for w in disease_List:
            if w not in stopwords.words('english'):
                filtered.append(w)
        Rfiltered = nltk.pos_tag(filtered)
        for j in range(len(Rfiltered)):
            fp.write(Rfiltered[j][0]+' ')
        fp.write(',' + df.iat[i, 3].astype(str) + '\n')
    fp.close()
    print('Seperate ' + read_path + '\\' + file + ' DONE')
print('Seperate successfully!')

"""
    for i in range(len(df)):
        text = df.iat[i, 1] + ' '+ df.iat[i, 2]
        words = word_tokenize(text)
        fp.write(df.iat[i, 0].astype(str) + ',')
        # wordsFiltered = []
        for w in words:
            if w not in stopWords:
                fp.write(w + ' ')
                # wordsFiltered.append(w)
        # print(wordsFiltered)
        fp.write(',' + df.iat[i, 3].astype(str) + '\n')
    fp.close()
    print('@@@@@@@@@@@' + read_path+file + ' DONE')
"""
