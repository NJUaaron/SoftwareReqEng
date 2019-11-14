# coding=utf-8
 
import requests#导入requests包
from bs4 import BeautifulSoup#从bs4导入beautifulsoup包
import time
import random

import re
import csv
# 获取html文档的函数，下面会调用

data=[]
csvdata=[]
csvdata.append(['ID','Title','Content'])
COUNT=1

p1=0
p2=0
p3=0
p4=0
p5=0

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
def get_certain_content(html):
    global COUNT
    soup = BeautifulSoup(html, 'lxml')#使用lxml解析器对网页进行解析（可以使用默认解析器，但是lxml解析器功能更加强大）
    #print(soup)
    head=soup.select('title')
    strinfo=re.compile(r'(<title>)|(</title>)')
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

def lab2_get_content(html):
    global p1,p2,p3,p4,p5
    soup = BeautifulSoup(html, 'lxml')#使用lxml解析器对网页进行解析（可以使用默认解析器，但是lxml解析器功能更加强大）
    #print(soup)
    head=soup.select('title')
    strinfo=re.compile(r'(<title>)|(</title>)')
    #print(head)
    result_head=strinfo.sub('',str(head))
    #print(result_head)
    id,title=result_head.split(" – ",1)

    strinfo=re.compile(r'[^a-zA-Z0-9]')
    title=strinfo.sub(' ',str(title))
    
    #print(id)
    #print(title)


    importance=soup.find_all("td")
    for k in importance:
        #print(k)
        level=re.findall(r'P[1-9]',str(k))
        if len(level):
            #print(level[0][1])
            break
    content=soup.select('#c0 .bz_comment_text')
    #print(content)
    strinfo=re.compile(r'(<.+>)|(</.+>)|(at .+\.)|\n|\t')#|(\/?((\w|\.)+\/?)+)')
    result=strinfo.sub('',str(content))
    strinfo=re.compile(r'[^a-zA-Z0-9]')
    result=strinfo.sub(' ',str(result))
    #print(result)

    if level[0][1]==str(1):
        p1=p1+1
    if level[0][1]==str(2):
        p2=p2+1
    if level[0][1]==str(3):
        p3=p3+1
    if level[0][1]==str(4):
        p4=p4+1
    if level[0][1]==str(5):
        p5=p5+1

    #print(id[1:])
    #print(title[:-1])
    #print(result)
    #print(level[0][1])
    data.append([id[1:],title[:-1],result,level[0][1]])

def print_level():
     global p1,p2,p3,p4,p5
     print(p1)
     print(p2)
     print(p3)
     print(p4)
     print(p5)


if __name__ == '__main__':
    """
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
                get_certain_content(certain_html)
        if page%10==9:
            time.sleep(5)"""

    
    #page_url="https://bugs.eclipse.org/bugs/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&field0-0-0=product&field0-0-1=component&field0-0-2=alias&field0-0-3=short_desc&field0-0-4=status_whiteboard&field0-0-5=content&limit=0&order=bug_status%20DESC%2Cpriority%2Cassigned_to%2Cbug_id&query_format=advanced&type0-0-0=substring&type0-0-1=substring&type0-0-2=substring&type0-0-3=substring&type0-0-4=substring&type0-0-5=matches&value0-0-0=ide&value0-0-1=ide&value0-0-2=ide&value0-0-3=ide&value0-0-4=ide&value0-0-5=%22ide%22"
    #print(page_url)
    #page_html=get_html(page_url)
    #soup = BeautifulSoup(page_html, 'lxml')#使用lxml解析器对网页进行解析（可以使用默认解析器，但是lxml解析器功能更加强大）
    #print(soup)

    #id_list=soup.find_all("td",{"class":"first-child bz_id_column"},limit=2)
    #strinfo=re.compile(r'(<title>)|(</title>)')
    #result_head=strinfo.sub('',str(head))
    with open("id1.csv", "r",encoding='utf-8') as f:
        all_id = csv.reader(f)
        stop=0
        file_number=1
        for line in all_id:
            each_address="https://bugs.eclipse.org/bugs/show_bug.cgi?id="+line[0]
            print(each_address)
            certain_html=get_html(each_address)
            lab2_get_content(certain_html)
            stop=stop+1
            file='raw'+str(file_number)+'.csv'
            csv_write(file,data)
            #print_level()
            if stop%10==0:
                time.sleep(5)
            if stop%500==0:
                random.shuffle(data)
                csv_write(file,data)
                
                print_level()

                file_number=file_number+1
                data.clear()
                

    """
    for each_id in id_list:
        each_id=re.findall(r'href="([^"]+)"',str(each_id))
        print(each_id)
        each_address="https://bugs.webkit.org/"+each_id[0]
        print(each_address)
        certain_html=get_html(each_address)
        lab2_get_content(certain_html)
    """
    #csv_write('test.csv',data)
    
    """
    url="https://bugs.webkit.org/show_bug.cgi?id=138248"
    html=get_html(url)  
    lab2_get_content(html)
    """

   
    

    """
    soup = BeautifulSoup(html, 'lxml')
    #get_certain_content(html)
  
    importance=soup.find_all("td")
    for k in importance:
        #print(k)
        level=re.findall(r'P[1-5]',str(k))
        if len(level):
            print(level)
    content=soup.select('#c0 .bz_comment_text')
    print(content)
    strinfo=re.compile(r'(<.+>)|(</.+>)|\n')#|(\/?((\w|\.)+\/?)+)')
    result=strinfo.sub('',str(content))
    print(result)
    """
    #csv_write('manual.csv',data)
    #csv_write('raw.csv',csvdata)
    
    
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