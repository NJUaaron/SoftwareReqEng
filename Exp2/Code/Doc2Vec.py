import gensim
from os import listdir

# 先把所有文档的路径存进一个 array 中，docs：
docs = [f for f in listdir("Data/Word.csv") if f.endswith('.csv')]

LabeledSentence = gensim.models.doc2vec.LabeledSentence  # 句標簽

docLabels = []
paragraph = []

# 把所有文档的内容存入到 paragraph 中，重要度存入標簽：
for doc in docs:
    file = open("./" + doc, 'r', encoding='utf8')
    # data.append(open("./" + doc, 'r',encoding='utf8')) # append接續在列表末尾，不換行
    # 讀入格式 序號，分詞結果字符串，等級
    raw_doc = file.read()
    file.close()
    List = raw_doc.split('\n')  # 先按行分割
    for i in range(len(List)):
        List[i] = List[i].split(',')  # 按逗號分割
        print(List[i])
        docLabels.append(List[i][2])  # 把重要度當作標簽
        paragraph.append(List[i][1])  # 把段落存入數組
    # return List


# 文檔集合訓練模型
class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):  # 迭代器
        for i, doc in enumerate(self.doc_list):
            yield LabeledSentence(words=paragraph[i].split(), labels=[self.labels_list[i]])


'''
数据：多个文档，以及它们的标签，可以用标题作为标签。
影响模型准确率的因素：语料的大小，文档的数量，越多越高；文档的相似性，越相似越好。

實現思路
1. 把每行輸入的分詞當作段落，計算句向量？
2. 將重要程度當作標簽？
'''

it = LabeledLineSentence(paragraph, docLabels)

model = gensim.models.Doc2Vec(size=50, window=10, min_count=5, alpha=0.025, min_alpha=0.025)
# dbow (distributed bag of words) dm = 0
# dm (distributed memory) dm = 1
model.build_vocab(it)  # 建立句向量模型

for epoch in range(10):  # 訓練模型迭代十次?
    model.train(it)
    model.alpha -= 0.002  # decrease the learning rate
    model.min_alpha = model.alpha  # fix the learning rate, no deca
    model.train(it)

print('Model Build Complete! Model shape : ', model.wv.syn0.shape)
for i in range(model.wv.syn0.shape[0]):
    print(model.wv.index2word[i])

# model.save("doc2vec.model")
''' model test '''
# model.similar_by_vector('''' "Document name" ''')

''' Save to CSV '''
f = open('./Data/vec.csv', 'w')
senVec_num = 1
for senVec in senVec_list:
    f.write(str(senVec_num))
    f.write(',')
    for i in range(len(senVec)):
        if i != 0:
            f.write(',')
        f.write(str(senVec[i]))
    f.write("\n")
    senVec_num = senVec_num + 1
f.close()
print('vec.csv save complete !')
