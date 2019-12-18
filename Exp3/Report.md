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
我们选定需求[**Code inset feature #66418**](https://github.com/microsoft/vscode/pull/66418)，用Python对该需求进完成爬虫后，我们基于爬虫得到的数据进行分析。该issue在2019.1.12由[**rdeline**](https://github.com/rdeline)创建，初始需求是希望vscode实现一个新的feature，允许将HTML文件内嵌在编辑器的代码行中。这个新feature对外提供一些接口供插件调用，从而实现一些各式各样的功能。

在2019.1.24，需求提出者rdeline又提供了一些需求的细节。这个feature需要使用网页预览元件来实现，并且提供代码和网页视图之间的交流渠道。因此，网页视图中托管的JS代码可以发布供扩展程序监听的消息。内联文档扩展可以使用此方法来传达HTML内容的大小。

在2019.2.12，团队完成了[**Code Inset Feature**](https://github.com/microsoft/vscode/pull/66418/commits/066dfef8f70379c9d4d8fbf3d2d4d0a2259c331e)。并在后续做了一些代码上大大少少的修改，完成了需求的基本功能，然后merge到了master上。

随后，在2019.2.13，issue的参与者[**jrieken**](https://github.com/jrieken)指出这个issue还没有被彻底解决，提出了以下2条需要改进的地方：

* Lifecycle - each web view is a process, a single editor cannot have 10s or 100s. We should consider (a) restarting, e.g. only visible insets are running, (b) adding a non-interactive inset, no code execution which would allow for an iframe, (c) limit the number of insets

* API - the current proposal is very much like code lens. The flow is that whenever a text inside the editor changes, we ask for the places at which insets will occur and then we ask to fill those insets. We should study the use-cases but a "push" API might be better. E.g. have something like *createTextEditorInset(editor, position, options)* which an extension calls whenever it wants to add an inset (when a command is invoked or when text changes). The extension will then manage insets as long as the editor exist - this approach is similar to editor decorations.

对于jrieken提出的改进，rdeline在2019.2.14对原始需求进行一些修改以及补充，强调对文本和图像内容展示的优化，以及对interactive inset的支持。此处发生了**需求的变动**。

需求发生变动后，团队对新提出的需求进行了一些讨论，表示支持。之后在2019.6.20完成了[**more code insets API tweaks**](https://github.com/microsoft/vscode/commit/5c3bab92ac05e8e1fb33d77fad154f4314d39f14)，实现了相关的需求。到现在为止，该issue还没有结束，因此需求今后依然可能发生变动。


### 六、实验结果
经人工分析后，我们绘制出该需求的变动时间线，跟踪了需求提出的事件、提出者,项目参与者对需求的变更与讨论。该需求仅实现了部分功能，仍有一些提案仍在讨论中。  
![时间线](https://github.com/NJUaaron/SoftwareReqEng/blob/master/Exp3/Figure/Timeline.png)
