# 软件需求工程
## 实验一 软件需求的抽取与分类

### 一、实验目标
&emsp;&emsp;实现软件需求的抽取与分类。

### 二、实验人员
* 161220085 刘心悦（25%）
* 171860595 陈少谦（25%）
* 171860663 马少聪（25%）
* 171860681 冯旭晨（25%）

### 三、实验思路 
&emsp;&emsp;**Stack Overflow**是开发者进行问答的著名网站，上面存在大量的有关软件开发的优秀问答。本次实验中我们用“IDE”作为标签进行搜索，使用爬虫找到所有[IDE相关的问答](https://stackoverflow.com/questions/tagged/ide)。我们将网站上的每一个问答视为一个 Smart IDE 的潜在需求，直接对问答进行分类。分类完成后，我们再对每一类文本进行词云分析，提取出若干关键字作为参考，帮助并对每一类进行分析，探究不同类别需求之间的异同。

&emsp;&emsp;要完成以上任务，我们需要依次实现爬虫、分类和词云的功能。其中分类步骤是比较困难的，选择不同的分类方法难度迥异，且最后的分类效果也千差万别。本次实验中我们尝试使用与传统的邮件分类相似的方法————先分词，再将词转换成词向量，然后得到段落的向量，最后再用聚类方法按照向量在高维词空间中的分布对需求进行划分。


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
4. 聚类
   1. 聚类采用的是最简单常用的kmeans算法，使用了sklearn中的cluster包
   2. 从vec.csv文件中读入处理好的段落向量，进行聚类
   3. 分好类的文本信息存放在classification文件夹中，每一个文件存放一个类别的文本信息
5. 词云分析
   1. 首先使用Python自带的collections包中的Counter函数，计算每个单词的词频
   2. 将词频最高的若干个单词（如30个）按照“单词:词频”的格式输出到txt文件中
   3. 将txt文件中的词频信息放到在线词云制作网站[WordItOut](http://www.yyyweb.com/demo/inner-show/word-itout.html)上，生成最终的词云

### 五、文件说明
1. 爬虫  
    &emsp;&emsp;爬虫功能实现在Crawler.py中。爬虫读取Stackoverflow上的信息，将每一条问答作为一条记录，存放在raw.csv中，其中每一行代表一条记录，格式为每行三列，分别是序号/问题标题/问题答案。<br>
    &emsp;&emsp;首先利用get_html函数获得每页链接的网页源码，接着使用get_address函数获取每页中各个问题的地址，对于每个问题的地址，利用循环分别进行访问。在循环中，再次利用get_html函数访问得到网页源码，get_certain_qa函数得到每个问题网页的具体标题、问题和回答。

2. 分词  
    &emsp;&emsp;分词功能实现在Separate.py中。文件读取raw.csv，输出分词文件word.csv。其中每一行代表一条记录，记录中的分好的单词之间用逗号隔开。  

3. 词转词向量  
    &emsp;&emsp;词转词向量功能实现在Word2vec.py中。文件读取分词文件word.csv，输出词向量文件vec.csv。其中每一行代表一条记录的向量，向量的每个分量之间用逗号隔开。  

4. 聚类
    &emsp;&emsp;聚类功能实现在Aggregate.py中。文件读取词向量文件vec.csv，将所有记录分成若干类，再将raw.csv和word.csv中的信息按照记录分好的类别，存放到不同文件中，每个文件代表一个类别的记录。这些分类文件在classification文件夹中。从raw.csv中分出来的记录以“class数字.csv”的格式存放；从word.csv中分出来的记录以“class_w_数字.csv”的格式存放。
    
5. 词频分析  
    &emsp;&emsp;聚类功能实现在Frequency.py中。文件读取分类文件class_w_数字.csv，输出该文件中出现次数最多的若干单词及其词频，以“class_w_数字_c.txt”的格式存放在classification文件夹中。词频分析的图片结果存放在Pictures文件夹中。

### 六、实验结果
1. 词云分析
    * class0: IDE / code / Eclipse / NetBeans / Delphi / Lazarus / Emacs / Visual Studio / Python / Java / Windows / Linux / Project / Problem <br>
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp1/Pictures/WordCloud0.png)
    * class1: IDE / code / Eclipse / NetBeans / Delphi / Editor / time / plugin / Android / Vim <br>
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp1/Pictures/WordCloud1.png)
    * class2: IDE / code / Eclipse / NetBeans / Emacs / Visual Studio / Selenium IDE / Windows / Linux / debugger / error / Java / Python / example <br>
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp1/Pictures/WordCloud2.png)
    * class3: IDE / code / Eclipse / Emacs / Vim / Java / error / command / command-line / folder / files / method / application <br>
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp1/Pictures/WordCloud3.png)
    * class4: IDE / code / Eclipse / NetBeans / Visual Studio / Python / Java / Windows / app / program / project / files / case / example <br>
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp1/Pictures/WordCloud4.png)

2. 需求分类
    * class0：PC端操作系统/ 编程语言 / 集成开发环境（IDE）
    * class1: 移动端操作系统 / 编辑器（Vim/Editor) / 外部插件
    * class2：调试器 / 应用程序测试 / 测试样例
    * class3: 文件资源管理器 / 命令行操作界面
    * class4: 项目管理器
       
3. 需求分析
     * 支持多种操作系统，如 Windows / Linux/ MacOS
     * 支持多种编程语言，如 Python / Java / C / C++ / HTML
     * 支持多种外部插件
     * 支持文件资源管理器 / 项目管理器 
     * 具有完备的调试/ 样例测试 / 程序测试等功能
     * 具有命令行操作功能
     * 功能强大的编辑器

### 七、反思改进
* 刘心悦：
    * 通过本次实验，我初次在学校体验与同学通过仓库进行分工合作，完成一个完整的项目。使用代码仓库进行协同开发真是非常有趣，当然这次实验中也有各种不周全的地方，没能和小伙伴一起配合得很完美。下次肯定就能做得更好啦~！
* 陈少谦：
    * 本次实验了解到了最基础的自然语言分析流程，同时实践了实际软件开发中需求获取的其中一个方式
    * 词转词向量这个部尚存在可改进的空间：由于本次实验数据集较小，故词向量的准确性有待提升
    * 实验过程中亦体会到协同开发中的细枝末节将影响开发效率，需要在开发前规定好分工/时间节点/文件接口等互通功能
* 马少聪：
    * 本次实验学习了爬虫/分词/词云分析/聚类等实验过程，了解了实际软件开发工作中的需求获取过程，掌握了一定的需求分析技术。
    * 在分词过程中的可改进之处是：
        * 本次分词采用了spacy的名词分词库，倘若可以进一步使用字典分词精细关键字筛选过程，实验结果将更加清晰显著。
        * 分词结果中出现了大量的I/He/She/what/which/some等代词及修饰词，干扰了词频分析。我利用正则表达式过滤掉了基本的代词，但因为正则表达式并不完全导致短语中的代词无法被过滤。
    * 实验过程中不仅学习了软件需求工程的内容，更深刻体会到类似软件工程中开发过程的问题，如实验流程安排/ 时间节点控制/ 文件接口协议等等。
* 冯旭晨：
    * 本次实验学习到了以前很感兴趣的关于爬虫的知识并且自己亲自动手完成了一个简单的爬虫程序
	* 在Python语言的编写上还不够熟练，写出来的爬虫程序略显笨重，没有体现Python语言的方便性。
    * 由于在Stack Overflow上对IDE搜索后只有约500条问答，收集到的信息数量比较少，最后得出的分析结果可能无法做到完全准确。

### 八、实验总结
&emsp;&emsp; 本次实验由于数据集不够大、算法过于简单，词向量求平均作为文章向量本身就超不靠谱，简单的kmeans作为聚类算法也不能很好反映数据的特征，导致分类效果並不显著。
