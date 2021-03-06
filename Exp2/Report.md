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
&emsp;&emsp;选定一个开源 IDE 项目，确定可能的信息来源，获取有效信息，对所获取的需求进行优先级排序。
（1） 确定 IDE 项目；
（2） 明确信息源；
（3） 获取需求；
（4） 提出一种方法，对需求进行优先级排序。

&emsp;&emsp;在本次实验中，我们选择了 Eclipse 这个IDE中的[缺陷报告](https://bugs.eclipse.org/bugs/)当作软件需求来源。这份数据中带有重要程度，以及bug的内容描述，所以我们决定使用机器学习的方法训练需求排序模型。本次实验采用的是深度神经网络模型（DNN）。模型训练完成后，我们使用准确率（Accuracy）来衡量其精度。为了使得到的结果可能更接近于分类器的真实性能，我们采用了10折交叉验证（10-fold）——将数据等量随机分为10份，使用其中9份的数据进行模型训练，剩下1份做模型验证；重复10次，每次的准确率取平均作为实验的最终结果。

&emsp;&emsp;完成上述任务分为以下几个步骤：
1. 爬虫：从网站爬取相应数据
2. 分词：将爬取的原始数据做预处理
3. 训练段落向量：将预处理后的分词文件放入模型训练
4. 训练神经网络模型：向量数据分为训练集和测试集，用训练集的数据对模型进行训练
5. 验证模型：模型对测试集数据进行预测，对预测结果进行评估


### 四、实验步骤
1. 爬虫  
    1. 打开[Eclipse](https://bugs.eclipse.org/bugs/)，构造访问问答界面的请求，获取页面内容进行解析。
    2. 在页面调用开发者工具，查看bug的编号、bug描述和等级所对应的HTML源码，确定编号、描述和等级所对应的类和标签。
    3. 利用beautifulsoup模块的select函数进行查找。
    4. 利用re的compile函数和strinfo的sub函数对筛选后的源码再次筛选，将多余的内容通过正则表达式删去。
    5. 将处理后的编号、bug描述和等级输出到文件，文件名为“X.csv”,X从0到9，格式为每行对应一条bug记录，每个文件对应500条数据。
2. 分词
    1. 爬虫得到的数据中，10个文件中的5种类别的数据量并不平均，故要首先将各类别数据统一到一起。通过Classify.py文件将Data/Raw文件夹中的10个文件中的每行按重要类别分为5个文件，存储在Data/Class中。
    2. 通过Average.py文件将5个类别的数据平均分配到10个文件中，存储在Data/NewRaw中。
    3. 通过Separate.py文件将NewRaw中的10个文件进行分词处理：
        1. 利用nltk库中的word_tokenize进行分词
        2. 再使用stopwords去除文本中的停用词，包括常用的代词、介词、疑问词等。
        3. 将分词结果分别写入Data/Word的10个文件中。
3. 词转词向量
   1. 从Data/Word中獲取10个分词文件，将其中的每一列分别读入对应数组中
   2. 使用gensim.doc2vec训练段落向量，将重要程度当作段落的标签放入向量维数为50的模型训练
   3. 将训练后的模型用段落对应的分词读取其段落向量并存入Data/Vec中
4. 模型训练
   1. 读取9个词向量文件作为训练集；剩下1个文件作为测试集
   2. 用训练集数据对DNN模型进行训练
   3. 用训练好的模型对测试集进行预测，与原本的优先级进行比对，计算出准确率



### 五、文件说明
1. 爬虫  
    &emsp;&emsp;爬虫功能实现在WebCrawler.py中。爬虫读取Eclipse上的bug信息，将每一条bug信息作为一条记录，存放在rawX.csv中，X从1到10，其中每一行代表一条记录，格式为每行四列，分别是bug编号/bug标题/bug描述/bug等级。<br>
    &emsp;&emsp;首先利用get_html函数获得bug列表网页的网页源码，接着使用get_address函数获取各个bug的地址，这里由于bug列表网页没有分页，一万多条跳转数据存放在一个网页中，如果使用get_html和get_address来获取各个bug的地址会非常缓慢，所以我将需要抓取的数据的bug编号复制下来，利用跳转网址和bug编号之间的联系直接访问每个bug的具体网页，略去了从bug列表网页中获取各个bug具体网页地址的过程。

2. 分词
    &emsp;&emsp;获得Data/Raw中的爬虫数据，按5种类别分类存储在Data/Class中，将5类数据平均分配在Data/NewRaw的10个文件中，对这10个文件处理的分词结果放在Data/Word的10个文件中。

3. 词转词向量  
    &emsp;&emsp;词转词向量功能实现在Code/Doc2vec.py中。读取10个分词文件，输出10个词向量文件vec0~9.csv。每个文件中的一行代表一段落对应的的向量，向量的每个分量之间用逗号隔开。  

4. DNN模型  
    &emsp;&emsp;DNN模型实现在Code/DNN.py中，借助TensorFlow进行模型的搭建。本次实验中DNN采用的是双隐层结构，第一个隐层节点数是30，第二个隐层节点数是15。训练算法为AdamOptimizer，损失函数为交叉熵（Cross Entropy），步长为0.0002，每一批从训练集中随机选择50条数据进行训练，迭代10000次。
    ```python
    #DNN parameters
    metrix_num = 50
    batch_size = 50
    hidden_layer_nodes1 = 30
    hidden_layer_nodes2 = 15
    step_length = 0.0002
    seed = tf.set_random_seed(2019)
    ```
    &emsp;&emsp;训练结束后，用模型对测试集的数据进行预测，并计算其准确率。由于本次实验中我们采用了10-fold，因此我们需要进行10次训练，再将得到的10次准确率结果求平均，作为最终的准确率，用来衡量我们模型的表现。  


### 六、实验结果  
&emsp;&emsp;DNN训练过程中，我们用交叉熵作为损失函数，并记录了每一轮迭代后训练集和测试集各自的交叉熵，记为<font color=red>Train Loss</font>和<font color=red>Test Loss</font>。下图为两者在训练过程中的变化情况。  
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp2/Pictures/LossPlot.png)  
&emsp;&emsp;图中横坐标为迭代次数，纵坐标为交叉熵的值。可以看到，随着训练的进行，Train Loss和Test Loss都在持续下降，其中Test Loss下降明显，并在迭代次数为10000次左右趋于平缓，模型达到一个较优的点。  
&emsp;&emsp;由于DNN预测的结果是一个小数，而不是像原本的优先级一样是一个整数，所以我们需要定义一个阈值X，只要满足：
```  
    正确值 - X <= 预测值 <= 正确值 + X    (X > 0)
```  
我们就认为预测值是准确的。  
&emsp;&emsp;为了更好地展示模型训练出来的结果，我们定义了3种准确率：accuracy1, accuracy2, accuracy3。它们分别是在X = 0.5, X = 1, X = 1.5的情况下计算出来的。以下是我们模型预测结果得到的三种准确率的值。  
![](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp2/Pictures/Accuracy.png)  
&emsp;&emsp;可见，虽然accuracy1比较低，只有0.3，但是accuracy2和accuracy3都处于较高水平。也就是说，大部分情况下，模型预测的优先级和真实优先级之间的差距不会超过1，可以算是非常令人满意的结果了。

### 七、反思改进
1.  冯旭晨：
    1.  由于Eclipse的bug列表网站本身的局限性，一万多条数据全部存放在一个网页中，导致真个网页加载速度十分缓慢，不得不把ID复制下载直接访问具体网页。
    2.  在访问Eclipse网站时，可能是网络本身的问题，有时候不练VPN就可以直接抓取数据，有的时候连上VPN还是会在抓取数据过程中连接断开。
    3.  数据本身分布不平均，P3的数据特别多而其他等级的数据量就很少，最后只能将一万多条数据中非P3的数据单独抓取下来。
2.  马少聪：
    1.  由于数据不平均会使得训练结果较差，故需要重构数据分布。
    2.  本次分词采用ntlk的库，筛选动词的效果不是很好，但优点是可通过修改本地停用词文件进行过滤，达到灵活控制的能力。
4. 刘心悦：
    1. 数据本身分布不平均，P3的数据占了非常大的比例，因此DNN会倾向将所有数据都预测成3附近的数字，造成准确率虚高。因此在以后的实践中，我们需要引入其他机器学习指标，来更全面地衡量分类器的效果。同时，我们也应该对DNN模型进行一些调整，使其能够对占小比例的数据（P3以外的数据）进行强化学习，得到更优秀的分类效果。

### 八、实验总结
&emsp;&emsp; 本次实验完成了对软件优先级的获取，并借助Google的TensorFlow框架搭建了DNN帮助我们对优先级进行排序，最后得到了令人满意的排序结果。
