import pandas as pd
import numpy as np
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('raw.csv', error_bad_lines = False, encoding='utf8')
fp = open('word.csv','w+', encoding='utf8')

for i in range(len(df)):
    words = []
    content = df.iat[i,1] + ',' + df.iat[i,2]
    doc = nlp(content)
    for nounc in doc.noun_chunks:
        words.append(nounc.text)
    print(words)
    
    for j in range(len(words)):
        fp.write(words[j])
        if j < len(words)-1:
            fp.write(',')
    fp.write('\n')

fp.close()
print("Separate words successfully!")
