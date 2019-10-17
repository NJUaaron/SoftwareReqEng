# import csv
import pandas as pd
import numpy as np
import spacy
nlp = spacy.load("en_core_web_sm")


df = pd.read_csv('test.csv', header = None, error_bad_lines = False, encoding='gb18030')
# df.columns = ['num', 'title', 'text']
print(df)
print()
for i in range(len(df)):
    words = []
    text = df.iat[i,1] + ',' + df.iat[i,2]
    doc = nlp(text)
    for nounc in doc.noun_chunks:
        words.append(nounc.text)
    print(words)
    print()
    string = ""
    for j in range(len(words)):
        string = string + "".join(words[j]) 
        string = string + ","
    string = string[:-1]
    print(string)
    print()
    df.iat[i,2] = string

print(df)
df.to_csv('result.csv', header = 0, index = 0)