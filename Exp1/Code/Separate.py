import pandas as pd
import numpy as np
import spacy
import re

patn = re.compile(r'^[Tt]he\b ?|^[Aa]\b ?|^[Aa]n\b ?|^I\b ?|^[Mm]e\b ?|^[Yy]ou\b ?|^[Hh]e\b ?|^[Ss]he\b ?|^[Ii]t\b ?|^[Ww]e\b ?|^[Tt]hey\b ?|^[Mm]y ?|^[Yy]our ?|^[Hh]is ?|^[Hh]er ?|^[Tt]heir\b ?|^[Ww]hat ?|^[Ww]ho ?|^[Ww]here ?|^[Ss]ome ?|^[Aa]ll\b ?|^[Aa]ny\b ?|^[Oo]ne ?|^[Tt]his\b ?|^[Tt]hat\b|^[Ss]uch a ?|^[Ss]o\b ?')
nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('..//Data//raw.csv', error_bad_lines = False, encoding='utf8')
fp = open('..//Data//word.csv','w+', encoding='utf8')

for i in range(len(df)):
    words = []
    content = df.iat[i,1] + ',' + df.iat[i,2]
    doc = nlp(content)
    for nounc in doc.noun_chunks:
        words.append(nounc.text)
    # print(words)
    
    for j in range(len(words)):
        string = ""
        string = words[j]
        str = re.sub(patn, '', string)
        if len(str)>1:
            fp.write(str)
            if j < len(words)-1:
                fp.write(',')
    fp.write('\n')

fp.close()
print("Separate words successfully!")
