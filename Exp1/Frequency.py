#读入分词文件，输出词频较高的词语
from collections import Counter


def readcsv(filePath):
    wordList = []
    with open(filePath, 'r') as f:
        for line in f:
            for d in line.split(','):
                if d != '\n':
                    wordList.append(d)
    print("Word Read Complete!")
    return wordList


if __name__ == '__main__':
    #输入的分词文件
    fileName = "class_w_0"
    words = readcsv("Classification//" + fileName + ".csv")
    counter = Counter(words)

    # 打印前若干个高频词
    printNum = 30   #打印的高频词数量
    commonWords = counter.most_common(printNum)
    print(commonWords)
    with open("Classification//" + fileName + "_c.txt", 'w') as f:
        for pair in commonWords:
            f.write(pair[0] + ":" + str(pair[1]) + "\n")
    print("Save Frequency Complete!")
