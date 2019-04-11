from socket import  *
import sys
from lxml import etree
import datetime,time
import csv
import re
import requests
from bs4 import BeautifulSoup

csv_file=csv.reader(open('goodOrder.csv','r'))
a=[]
for i in csv_file:
    tmp=''
    for j in i:
        tmp=tmp+j
    if(tmp>'01100' and tmp<'01201'):
        a.append(tmp)
print(a)
totalData=[]
betterOrder=[]
count_t=0
headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

for count in a:
    url='http://services1.aastocks.com/web/bjty/CompanyFundamental.aspx?Language=Chn&category=FinRatio&symbol='+a[count_t]+'&yearType=Interim'
    html=requests.get(url)
    #htm=etree.HTML(message)
    soup = BeautifulSoup(html.content,'lxml')
    #comfund > table > tbody > tr.R0 > td > table > tbody > tr.R2 > td > table > tbody > tr.R2 > td > table > tbody > tr:nth-child(3) > td.IC1
    tmp1=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(3) > td.IC0')
    if(tmp1==[] or tmp1[0].get_text()!='流动比率(倍)'):
        count_t+=1
        continue
    tmp2 = soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(4) > td.IC0')
    if (tmp2==[] or tmp2[0].get_text() != '速动比率(倍)'):
        count_t+=1
        continue
    dat=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr.IRTitle >td.IC1')
    n=0
    for i in dat:
        tmp=[a[count_t]]
        tmp.append(i.get_text())
        datas=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(3) > td.IC'+str(n+1))
        for data in datas:
            tmp.append(float(data.get_text()))
        datas2=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(4) > td.IC'+str(n+1))
        for j in datas2:
            tmp.append(float(j.get_text()))
        totalData.append(tmp)
        n+=1
    time.sleep(0.5)
    url='http://services1.aastocks.com/web/bjty/CompanyFundamental.aspx?Language=Chn&category=FinRatio&symbol='+a[count_t]+'&yearType=Annual'
    html=requests.get(url)
    #htm=etree.HTML(message)
    soup = BeautifulSoup(html.content,'lxml')
    tmp1 = soup.select(
        '#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(3) > td.IC0')
    if (tmp1==[] or tmp1[0].get_text() != '流动比率(倍)'):
        count_t+=1
        continue
    tmp2 = soup.select(
        '#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(4) > td.IC0')
    if (tmp2==[] or tmp2[0].get_text() != '速动比率(倍)'):
        count_t+=1
        continue
    #comfund > table > tbody > tr.R0 > td > table > tbody > tr.R2 > td > table > tbody > tr.R2 > td > table > tbody > tr:nth-child(3) > td.IC1
    dat=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr.IRTitle >td.IC1')
    n=0
    for i in dat:
        tmp=[a[count_t]]
        tmp.append(i.get_text())
        datas=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(3) > td.IC'+str(n+1))
        for data in datas:
            tmp.append(float(data.get_text()))
        datas2=soup.select('#comfund > table > tr.R0 > td > table > tr.R2 > td > table > tr.R2 > td > table > tr:nth-child(4) > td.IC'+str(n+1))
        for j in datas2:
            tmp.append(float(j.get_text()))
        totalData.append(tmp)
        n+=1
    betterOrder.append(a[count_t])
    print(a[count_t])
    count_t+=1
    time.sleep(0.5)
with open('financialReport.csv', 'a+', newline='') as f:
    writer = csv.writer(f)
    for row in totalData:
        writer.writerow(row)
    f.close()
with open('betterOrder.csv', 'a+', newline='') as f:
    writer = csv.writer(f)
    for row in betterOrder:
        writer.writerow(row)
    f.close()


