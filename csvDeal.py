import csv
import datetime
"""
#把'/'替换成'-'
csv_file=csv.reader(open('financialReport.csv','r'))
tmp=[]
for i in csv_file:
    x=i[1].replace('/','-')
    tmp.append([i[0],x,i[2],i[3]])
with open('fincialReportAfter.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in tmp:
        writer.writerow(row)
    f.close()

"""
"""
csv_file=csv.reader(open('stockFinancial.csv','r'))
stock=[]
for i in csv_file:
    stock.append(i)
del stock[0]
print(stock)
csv_file=csv.reader(open('fincialReportAfter.csv','r'))
report=[]
for i in csv_file:
    report.append(i)
print(report)
totalData=[['股票编号','日期','收盘价','涨跌幅','换手率','流动比率','速动比率']]
for i in report:
    flag=0
    for j in stock:
        if j[0]==i[0]:
            flag=1
            if j[1]==i[1]:
                tmp=[i[0],i[1],j[2],j[3],j[4],i[2],i[3]]
                totalData.append(tmp)
        else:
            if flag==1:
                break
print(totalData)
with open('finalData.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in totalData:
        writer.writerow(row)
    f.close()
"""
"""
def cmp_datetime(a, b):
    a_datetime = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    b_datetime = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

    if a_datetime > b_datetime:
        return -1
    elif a_datetime < b_datetime:
        return 1
    else:
        return 0

csv_file=csv.reader(open('finalData.csv','r'))
stock=[]
for i in csv_file:
    stock.append(i)
del stock[0]
print(stock)
csv_file=csv.reader(open('priceData.csv','r'))
price=[]
for i in csv_file:
    price.append(i)
print(price)
totalData=[['股票编号','日期','收盘价','涨跌幅','换手率','基本每股收益','流动比率','速动比率']]
order=[]

for i in price:
    flag=0
    for j in stock:
        if j[0]==i[0]:
            flag=1
            if j[1]==i[1]:
                tmp=[j[0],j[1],j[2],j[3],j[4],i[2],j[5],j[6]]
                totalData.append(tmp)
        else:
            if flag==1:
                break
print(order)
print(totalData)
totalData2=totalData
totalData3=[]
tmp=[]
del totalData2[0]
last=totalData2[0][0]
for i in totalData2:
    if i[0]!=last:
        totalData3.append(tmp)
        last=i[0]
        tmp=[]
        tmp.append(i)
    else:
        tmp.append(i)
print(totalData3)
for i in totalData3:
    i.sort(key=lambda x:x[1],reverse=False)
print(totalData3)
for i in totalData3:
    order.append(i[0][0])
print(order)
with open('finalDataWithPrice.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in totalData3:
        writer.writerow(row)
    f.close()
with open('finalOrderwithPrice.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in order:
        writer.writerow(row)
    f.close()
"""

