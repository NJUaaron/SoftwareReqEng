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
    words = readcsv("Classification//class_w_0.csv")
    counter = Counter(words)

    # 打印前20高频词
    print(counter.most_common(20))
