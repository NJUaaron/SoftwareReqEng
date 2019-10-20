# coding=utf-8
 
import requests#导入requests包
from bs4 import BeautifulSoup#从bs4导入beautifulsoup包
import time

import re
import csv
# 获取html文档的函数，下面会调用

data=[]
data.append(['ID','Title','Question','Answer'])
csvdata=[]
csvdata.append(['ID','Title','Content'])
COUNT=1

def csv_write(path,data):
    with open(path,'w',encoding='utf-8',newline='') as final:
        writer = csv.writer(final,dialect='excel')
        for row in data:
            writer.writerow(row)
    return True

def get_html(url):
    """get the content of the url"""
    response = requests.get(url)#从链接获取所有的网页源码
    response.encoding = 'utf-8'#转化编码模式为utf-8
    return response.text#返回转化之后的源码
    
# 获取函数，下面会调用
def get_certain_joke(html):
    global COUNT
    soup = BeautifulSoup(html, 'lxml')#使用lxml解析器对网页进行解析（可以使用默认解析器，但是lxml解析器功能更加强大）
    #print(soup)
    head=soup.select('title')
    strinfo=re.compile(r'(<title>)|(</title>)|[|]|- Stack Overflow')
    result_head=strinfo.sub('',str(head))
    print(result_head)

    certain_question = soup.select('#question .post-text p')#获取属性class为"question"的内容（可以查看网页源码之后确定搜索的内容）
    strinfo=re.compile(r'(<p>)|(</p>)|((<code>).+(</code>))|((<strong>).+(</strong>))|((<em>).+(</em))|(<(a.+>).+(</a>))|(<.+>)|(</.+>)|\n')
    result_question=strinfo.sub('',str(certain_question))
    #print("Question:")
    #print(result_question)
    
    certain_answer=soup.select('#answers .post-text p')
    #print(certain_answer)
    #result_answer=str(certain_answer)
    
    strinfo=re.compile(r'(<p>)|(</p>)|((<code>).+(</code>))|((<strong>).+(</strong>))|((<em>).+(</em))|(<(a.+>).+(</a>))|(<.+>)|(</.+>)|\n')
    result_answer=strinfo.sub('',str(certain_answer))
    #print("Answer:")
    #print(result_answer)
    
    data.append([COUNT,str(result_head)[1:-1],str(result_question)[1:-1],str(result_answer)[1:-1]])
    
    content=str(result_question)[1:-1]+str(result_answer)[1:-1]
    strinfo=re.compile(r',')
    asv_head=result_head
    asv_head=strinfo.sub('',asv_head)
    result_content=strinfo.sub('',content)
    csvdata.append([COUNT,str(asv_head)[1:-1],result_content])
    COUNT=COUNT+1
    return result_head#返回得到的内容



def get_address(html):
    soup = BeautifulSoup(html,'lxml')
    address = soup.select('.question-hyperlink')
   
    #print(address)
    return address


if __name__ == '__main__':
    
    for page in range(1,35):
        page_url="https://stackoverflow.com/search?page=" + str(page)+"&tab=Relevance&q=ide"
        print(page_url)
        page_html=get_html(page_url)
        address=get_address(page_html)
        #print(address)
        for item in address:
            #print(item)
            certain_url=str(item).split(" ")[3]
            #print(certain_url)
            certain_url=re.findall(r'href="([^"]+)"',str(certain_url))
            #print(certain_url)
            if len(certain_url)!=0:
                #print(len(res[0]))
                certain_url="https://stackoverflow.com/"+certain_url[0]
                print(certain_url)
                certain_html=get_html(certain_url)
                get_certain_joke(certain_html)
        if page%10==9:
            time.sleep(5)
    csv_write('manual.csv',data)
    csv_write('raw.csv',csvdata)
    #url_joke = "https://stackoverflow.com/questions?tab=active&page=1"#网页地址
    #html = get_html(url_joke)#获取网页源码
    #joke_content = get_address(html)#获取内容 
    #print(joke_content[0])
    #res=re.findall(r'href="([^"]+)"',str(joke_content[0]))
    #print(res)
    #print (joke_content)#打印获取的内容
    #aaa="[<p>a class=\"question\" href=\"/questions/58413499/<code>what the fuck</code></p>\"\n]"
    #print(aaa)
    #print(aaa[1:-1])
    #strinfo=re.compile(r'\n')
    #bbb=strinfo.sub('',aaa)
    #print(bbb)