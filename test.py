from socket import  *
import sys
from lxml import etree
import time
import json
import urllib.request
import datetime,time
import csv
import re
"""
x=[]
data=[['股票代码','17-12-31','16-12-31']]
date1='17-12-31'
date2='16-12-31'
totalAcount='资产总额|1'
flag=0
error_data=[]
for i in range(500):
    x.append(str(i+1).zfill(5))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
for i in range(500):
    url='http://emweb.securities.eastmoney.com/PC_HKF10/FinancialAnalysis/PageAjax?code='+x[i]
    content=urllib.request.urlopen(url).read()
    message = content.decode("utf8")
    if message == '{"msg":"股票代码不合法"}':
        print(x[i]+'error')
        error_data.append(x[i])
    else:
        rst =content.decode("utf-8")
        rst_dict=json.loads(rst)
        l=rst_dict['zcfzb']
        for count in range(len(l)):
            if l[count][0]==date1: dateOrder1=count;  flag=1
            if l[count][0]==date2: dateOrder2=count;  flag=1
        if flag==1:
            for y in range(len(l[0])):
                if l[0][y]==totalAcount: acountColumn=y
            data.append([x[i],l[dateOrder1][acountColumn],l[dateOrder2][acountColumn]])
        else:
            print(x[i] + 'error')
            error_data.append(x[i])
        print(data[-1])
    time.sleep(2)
with open('stockFinancial.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
with open('wrongStock.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in error_data:
        writer.writerow(row)
"""
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Cookie':'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1555129389; Hm_lvt_1db88642e346389874251b5a1eded6e3=1554884514,1554952370,1554988383,1555127242; _ga=GA1.2.2103741969.1554779880; _gid=GA1.2.1978831027.1555127242; u=441555129383272; xq_a_token=c3ad928c32844dd1159fadf6b740202c98f57e08; xq_a_token.sig=gGiB0IGXSeuhdiVqcjKBnjxWBNE; xq_r_token=ad311bab2af18c96dcdf509d59414b94ef1f5d4a; xq_r_token.sig=ILfaBwMDJJsRbIEHItnGAJQP668; _gat=1; device_id=0b5ab0d0a69ecbe3c8e75994612c5a92; s=ex17chesrb'}
x=[]
data=[['股票代码','时间','开盘价','最高价','最低价','收盘价','涨跌幅','换手率']]
orderT=[]
for i in range(1200):
    x.append(str(i+1).zfill(5))
"""
url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=00001&begin=1554866347598&period=quarter&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
req = urllib.request.Request(url=url, headers=headers)
order=x[i]
content = urllib.request.urlopen(req).read()
message = content.decode("utf-8")
rst = content.decode("utf-8")
rst_dict = json.loads(rst)
print(len(rst_dict['data']['item']))
"""
for i in range(1200):
    url='https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol='+x[i]+'&begin=1555215798851&period=quarter&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
    #'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol='+x[i]+'&begin=1554866347598&period=quarter&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
    #'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol='+x[i]+'&begin=1555213673813&period=month&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
    req = urllib.request.Request(url=url, headers=headers)
    order=x[i]
    content = urllib.request.urlopen(req).read()
    message = content.decode("utf-8")
    rst = content.decode("utf-8")
    rst_dict = json.loads(rst)
    if(rst_dict['data']!={}):
        length = len(rst_dict['data']['item'])
        if(length>=18): #month 40
            for j in range(18):
                timeStamp=rst_dict['data']['item'][length-j-1][0]
                priceFirst=rst_dict['data']['item'][length-j-1][2]
                priceMax=rst_dict['data']['item'][length-j-1][3]
                priceMin=rst_dict['data']['item'][length-j-1][4]
                priceLast=rst_dict['data']['item'][length-j-1][5]
                percent = rst_dict['data']['item'][length - j - 1][6]
                change = rst_dict['data']['item'][length - j - 1][8]
                n=timeStamp/1000
                timeArray = time.localtime(n)
                otherStyleTime = time.strftime("%Y-%m", timeArray)
                data.append([order,otherStyleTime,priceFirst,priceMax,priceMin,priceLast,percent,change])
            orderT.append(order)
            print(order)
        #print(otherStyleTime)
    time.sleep(0.5)
with open('quarterstockFinancial.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    f.close()
with open('quartergoodOrder.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in orderT:
        writer.writerow(row)
    f.close()

#for i in rst_dict['data']['item']:
 #   print(i)

