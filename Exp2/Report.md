# 软件需求工程
## 实验二 软件需求的优先级排序

### 一、实验目标
&emsp;&emsp;实现软件需求的优先级排序。

### 二、实验人员
* 161220085 刘心悦（25%）
* 171860595 陈少谦（25%）
* 171860663 马少聪（25%）
* 171860681 冯旭晨（25%）

### 三、实验思路 



### 四、实验步骤
1. 爬虫  
    1. 打开[Stack Overflow](https://stackoverflow.com/)，构造访问问答界面的请求，获取页面内容进行解析。
    2. 在页面调用开发者工具，查看问题和答案所对应的HTML源码，确定问题和答案所对应的累和标签。
    3. 利用beautifulsoup模块的select函数进行查找。
    4. 利用re的compile函数和strinfo的sub函数对筛选后的源码再次筛选，将多余的内容通过正则表达式删去。
    5. 将处理后的标题、问题和答案输出到文件，文件名为“raw.csv”,格式为每行对应一条问答记录。
2. 分词
    1. 获得爬虫的文本信息
    2. 通过pandas库读入csv文件，将每行的问题标题和答案文本进行字符串拼接
    3. 通过spacy库提取字符串中的名词及短语
    4. 利用正则表达式去除短语中的冠词/代词/频率副词等
    5. 将处理后的分词用逗号分隔并输出到文件，文件名为“word.csv”，其格式为每行对应一条问答记录，列数由单词量决定
3. 词转词向量
   1. 获取分词后的文本信息：文件名“word.csv”，格式为每段落占一行，每行中的每列为词语/短语
   2. 将每个词自csv文件读取入二维数组，同样按照每行为段落，每列为词语/短语
   3. 通过gensim中的word2vec将数据训练为词向量，再将每段中的词向量加总取平均作为段落向量
   4. 将段落词向量存入csv文件“vec.csv”，格式为 序号/向量


### 五、文件说明
1. 爬虫  
    &emsp;&emsp;爬虫功能实现在WebCrawler.py中。爬虫读取Stackoverflow上的信息，将每一条问答作为一条记录，存放在raw.csv中，其中每一行代表一条记录，格式为每行三列，分别是序号/问题标题/问题答案。<br>
    &emsp;&emsp;首先利用get_html函数获得每页链接的网页源码，接着使用get_address函数获取每页中各个问题的地址，对于每个问题的地址，利用循环分别进行访问。在循环中，再次利用get_html函数访问得到网页源码，get_certain_qa函数得到每个问题网页的具体标题、问题和回答。

2. 分词  
    &emsp;&emsp;分词功能实现在Separate.py中。文件读取raw.csv，输出分词文件word.csv。其中每一行代表一条记录，记录中的分好的单词之间用逗号隔开。  

3. 词转词向量  
    &emsp;&emsp;词转词向量功能实现在Word2vec.py中。文件读取分词文件word.csv，输出词向量文件vec.csv。其中每一行代表一条记录的向量，向量的每个分量之间用逗号隔开。  


### 六、实验结果


### 七、反思改进


### 八、实验总结
