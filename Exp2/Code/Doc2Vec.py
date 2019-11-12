"""
数据：多个文档，以及它们的标签，可以用标题作为标签。
影响模型准确率的因素：语料的大小，文档的数量，越多越高；文档的相似性，越相似越好。

實現思路
1. 把每行輸入的分詞當作段落，計算句向量？
2. 將重要程度當作標簽？
"""

import gensim
from os import listdir


LabeledSentence = gensim.models.doc2vec.LabeledSentence  # 句標簽


# 文檔集合訓練模型
class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):  # 迭代器
        for i, doc in enumerate(self.doc_list):
            yield LabeledSentence(words=paragraph[i].split(), labels=[self.labels_list[i]])


# 先把所有文档的路径存进一个 array 中，docs：
docs = [f for f in listdir("./Data/Word") if f.endswith('.csv')]


# 把所有文档的内容存入到 paragraph 中，重要度存入標簽：
idx = 1
for doc in docs:
    # 單個文件處理

    docLabels = []
    paragraph = []

    # 讀文件
    file = open(doc, 'r', encoding='utf8')
    # data.append(open("./" + doc, 'r',encoding='utf8')) # append接續在列表末尾，不換行
    # 讀入格式 序號，分詞結果字符串，等級
    raw_doc = file.read()
    file.close()

    # 預處理
    count = 0 # 段落數 後面保存時使用
    List = raw_doc.split('\n')  # 先按行分割
    for i in range(len(List)):
        List[i] = List[i].split(',')  # 按逗號分割
        print(List[i])
        docLabels.append(List[i][2])  # 把重要度當作標簽
        paragraph.append(List[i][1])  # 把段落存入數組
        count = i #計算段落數
    # return List

    #標簽化
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
    filename = idx +".csv"
    f = open("./Data/"+ filename, 'wb')
    for num in range(0, count):
        doc_vec = model.docvecs[num]
        f.write(doc_vec)
        # print num
        # print doc_vec
    f.close()
    print('vecter file'+ filename+' save complete !')
    # 單個文件處理

    idx = idx+1
    # 總共處理十次


'''
save(fname_or_handle, separately=None, sep_limit=10485760, ignore=frozenset({}), pickle_protocol=2)
    Save the object to a file.

    Parameters
    fname_or_handle (str or file-like) 
    – Path to output file or already opened file-like object. If the object is a file handle, no special array handling will be performed, all attributes will be saved to the same file.

    separately (list of str or None, optional) 
    –If None, automatically detect large numpy/scipy.sparse arrays in the object being stored, and store them into separate files. This prevent memory errors for large objects, and also allows memory-mapping the large arrays for efficient loading and sharing the large arrays in RAM between multiple processes.

      If list of str: store these attributes into separate files. The automated size check is not performed in this case.

    sep_limit (int, optional) 
    – Don’t store arrays smaller than this separately. In bytes.

    ignore (frozenset of str, optional) 
    – Attributes that shouldn’t be stored at all.

    pickle_protocol (int, optional) – Protocol number for pickle.
    
gensim.utils.save_as_line_sentence(corpus, filename)
    Save the corpus in LineSentence format, 
    i.e. each sentence on a separate line, tokens are separated by space.

    Parameters
        corpus (iterable of iterables of strings) –
'''