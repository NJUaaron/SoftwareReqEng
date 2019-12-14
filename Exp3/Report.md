# 软件需求工程
## 实验三 软件需求的跟踪分析

### 一、实验目标
&emsp;&emsp;对软件需求进行跟踪分析。

### 二、实验人员
* 161220085 刘心悦（25%）
* 171860595 陈少谦（25%）
* 171860663 马少聪（25%）
* 171860681 冯旭晨（25%）

### 三、实验思路 
* 选定一个开源 IDE 项目，确定一个软件需求 R，从该软件需求提出开始。 
* 明确提出需求 R 的文本，获取需求 R 的有关讨论文本； 
* 识别出实现需求 R 的代码； 
* 如果需求有变更，识别出需求变更： 
    * 明确需求变更的文本； 
    * 识别出与需求变更有关的代码； 
* 给出需求 R 的全生命周期的时间线。

### 四、实验步骤
1. [**Github**](https://github.com/)是目前众多开源项目使用的代码管理平台，该平台具有在线用户多、维护项目多、代码量大、代码管理好、操作简单等优点，其 `Issue / Pull Request / Merge` 机制极大地符合了需求管理的控制流程。基于以上特性，我们选择在Github平台上寻找开源项目进行本次实验。

2. **Visual Studio Code**（以下简称VScode）是一个轻量且强大的跨平台开源代码编辑器（IDE），支持Windows，OS X和Linux。内置JavaScript、TypeScript和Node.js支持，而且拥有丰富的插件生态系统，可通过安装插件来支持C++、C#、Python、PHP等其他语言。  
故我们选择了在Github上的[**Microsoft / VScode**](https://github.com/microsoft/vscode)开源项目作为实验素材。

3. 由于要研究开源项目的需求变更，而在Github中的一个需求提出常常是一个带有`feature-request`标签的`Issue`，完成一个需求后将通过`Pull Request`提交实现代码，若经过项目发起者的检验测试后确认该功能已实现便关闭该`Issue`。  
于是我们通过`Pull Request` & `closed` & `feature-request` & `Most Commented`标签选定了[**Code inset feature #66418**](https://github.com/microsoft/vscode/pull/66418)需求。

4. 利用自动化方法（Python数据爬虫）获取该PR中的详细信息，以该PR的标题为文件名，爬取相关讨论的文本信息和代码更新情况，同时提取出讨论中的相关网络链接和时间信息，以时间、文本内容、网络链接三列形成相应的文件，从而进行下一步的人工分析。代码存放于Code文件夹，爬取数据存放于Data文件夹中。

5. 通过爬取的信息人工分析该需求的变化过程、相应部分代码更新、需求完成现状等。

6. 根据爬取的信息分析并绘制该需求变更的时间线。

### 五、需求分析
1. 初始需求：


### 六、实验结果
![时间线](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp3/Figure/Timeline.png)
