from socket import  *
import sys
from lxml import etree
import time
import json
import urllib.request
import datetime,time
import csv
import re
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Cookie':'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1554779921; Hm_lvt_1db88642e346389874251b5a1eded6e3=1553440045,1554779880; _ga=GA1.2.2103741969.1554779880; _gid=GA1.2.2101156218.1554779880; device_id=0b5ab0d0a69ecbe3c8e75994612c5a92; u=551554779882402; xq_a_token=6793401481303b0b4078c00acf521f116693ab76; xq_a_token.sig=kn3AtIz_AxxI0iAzWFBkTMIOFfQ; xq_r_token=e5e64b239ced9de9b2e1d1b37182159946e08cf0; xq_r_token.sig=Qc9zNevVZNNCDpgFt-leV4WiA0E; s=ex17chesrb'}
csv_file=csv.reader(open('betterOrder.csv','r'))
stock=[]
for i in csv_file:
    tmp = ''
    for j in i:
        tmp = tmp + j
    stock.append(tmp)
x=[]
count_t=0
allData=[]
orderData=[]
print(stock)
"""
url='http://stock.finance.sina.com.cn/hkstock/api/jsonp.php/var%20tableData%20=%20/FinanceStatusService.getFinanceStatusForjs?symbol=00013&financeStatus=all'
req = urllib.request.Request(url=url, headers=headers)
content = urllib.request.urlopen(req).read()
rst = content.decode("utf-8")
rst_new=rst[49:]
rst_second=rst_new.strip('var tableData=')
if rst_second=='(null);':
    print('a')
else:
    print(rst_second)
"""
for z in stock:
    url='http://stock.finance.sina.com.cn/hkstock/api/jsonp.php/var%20tableData%20=%20/FinanceStatusService.getFinanceStatusForjs?symbol='+stock[count_t]+'&financeStatus=all'
    req = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(req).read()
    rst = content.decode("utf-8")
    rst_new=rst[49:]
    rst_second=rst_new.strip('var tableData=')
    if rst_second=='(null);':
        count_t+=1
        continue
    rst_second=rst_second.strip('(')
    rst_second=rst_second.strip(');')
    rst_second=rst_second[1:-1]
    rst_third=re.findall((r'(.*?)[,]'),rst_second)
    myList=[]
    tmp=[]
    for i in rst_third:
        if re.match(r'(.*?)[-](.*?)[-]',i):
            myList.append(tmp)
            tmp=[]
        tmp.append(i)
    del myList[0]
    myData=[]
    flag=0
    for i in myList:
        if i[10][1:-1]=='ul':
            flag=1
            break
        myData.append([stock[count_t],i[0][2:-4],float(i[10][1:-1])])
    if flag==1:
        count_t+=1
        continue
    allData.append(myData)
    orderData.append(stock[count_t])
    print(stock[count_t])
    count_t+=1

with open('priceData.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in allData:
        for i in row:
            writer.writerow(i)
    f.close()
with open('moreBetterOrder.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in orderData:
        writer.writerow(row)
    f.close()

#rst_dict=json.loads(rst_second)
#print(rst_dict)
