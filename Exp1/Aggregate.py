import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def readcsv(filePath):
    vecList = []
    with open(filePath, 'r') as f:
        for line in f:
            row = []
            serialNo = True
            for d in line.split(','):
                #Jump over the serial No
                if not serialNo:
                    row.append(float(d))
                else:
                    serialNo = False
            vecList.append(row)
    print("Wordvec Read Complete!")
    return vecList

def aggregate(X, n):
    #Kmeans Prediction
    kmeans = KMeans(n_clusters=ClustersNum).fit(X)
    pred = kmeans.predict(X)
    #print(pred)

    #Classification information
    C = []
    for type in range(n):
        C.append([i for i,x in enumerate(pred) if x == type])
    print(C)
    print("Kmeans Prediction Complete!")
    return C

def savecsv(Class, n):
    #Read raw file
    rawFile = open("raw.csv", encoding='utf8')
    rawDocument = rawFile.read()
    rawFile.close()

    #Line List
    L = rawDocument.split('\n')

    #Seperate raw data into different csv file by Class
    for type in range(n):
        saveFileName = "class"
        f = open("Classification\\" + saveFileName + str(type) + ".csv", 'w', encoding='utf8')
        Class_t = Class[type]
        for index in Class_t:
            if index + 1 < len(Class_t):
                f.write(L[index + 1])
                f.write("\n")
        f.close()

    print("Seperate Output Complete!")


if __name__ == '__main__':
    content = readcsv("vec.csv")
    ClustersNum = 10
    Class = aggregate(content, ClustersNum)
    savecsv(Class, ClustersNum)

    # plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='label0')
    # plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='label1')
    # plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='label2')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.legend(loc=2)
    # plt.show()
