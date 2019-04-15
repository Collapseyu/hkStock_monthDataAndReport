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
csv_file=csv.reader(open('quarterstockFinancial.csv','r'))
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
totalData=[['股票编号','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','流动比率','速动比率']]
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
#添加流动资产信息
csv_file=csv.reader(open('quarterFinalDataWithPrice.csv','r'))
stock=[]
for i in csv_file:
    stock.append(i)
del stock[0]
print(stock)
csv_file=csv.reader(open('eastReportasset.csv','r'))
price=[]
for i in csv_file:
    price.append(i)
print(price)
totalData=[['股票编号','报告日期','日期','收盘价','涨跌幅','换手率','日期','收盘价','涨跌幅','换手率','基本每股收益','流动比率','速动比率']]
"""

#添加每股基本收益
def cmp_datetime(a, b):
    a_datetime = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    b_datetime = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

    if a_datetime > b_datetime:
        return -1
    elif a_datetime < b_datetime:
        return 1
    else:
        return 0

csv_file=csv.reader(open('monthFinalData.csv','r'))
stock=[]
for i in csv_file:
    stock.append(i)
del stock[0]
print(stock)
csv_file=csv.reader(open('eastReportPrice.csv','r'))
price=[]
for i in csv_file:
    price.append(i)
print(price)
totalData=[['股票编号','日期','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','基本每股收益','流动比率','速动比率']]
#[['股票编号','报告日期','日期','收盘价','涨跌幅','换手率','日期','收盘价','涨跌幅','换手率','基本每股收益','流动比率','速动比率']]
order=[]

for i in price:
    flag=0
    for j in stock:
        if j[0]==i[0]:
            flag=1
            if j[1]==i[1]:
                tmp=[]
                for z in range(44):
                    tmp.append(j[z])
                    #tmp=[j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18],j[19],j[20],j[21],j[22],j[23],j[24],j[25],j[26],j[27],j[28],j[29],j[30],j[31],j[32],j[33],j[34],j[35],j[36],j[37],j[38],j[39],j[40],j[41],j[10],j[11],j[12],j[13],j[14],j[15],i[2],j[-2],j[-1]]
                tmp.append(i[2])
                tmp.append(j[-2])
                tmp.append(j[-1])
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

with open('monthFinalDataWithPrice.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in totalData3:
        writer.writerow(row)
    f.close()
with open('monthFinalOrderwithPrice.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in order:
        writer.writerow(row)
    f.close()

"""
#拼接财报数据（除每股基本收益）和季度或月度数据
csv_file=csv.reader(open('monthstockFinancial.csv','r'))
stock=[]
for i in csv_file:
    stock.append(i)
del stock[0]
#print(len(stock))
csv_file=csv.reader(open('fincialReportAfter.csv','r'))
report=[]
for i in csv_file:
    report.append(i)
last=report[0][0]
tmp=[]
reportAfter=[]
for i in report:
    if i[0]!=last:
        reportAfter.append(tmp)
        last=i[0]
        tmp=[]
        tmp.append(i)
    else:
        tmp.append(i)
for i in reportAfter:
    i.sort(key=lambda x:x[1],reverse=False)
print(reportAfter)
totalData=[['股票编号','日期','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','日期','开盘价','最高价','最低价','收盘价','涨跌幅','换手率','流动比率','速动比率']]
print(len(totalData[0]))
for i in reportAfter:
    date = i[0][1]
    for j in i:
        flag=0
        tmp=[]
        for m in stock:
            if m[0]==j[0]:
                flag=1
                if m[1]>date and m[1]<=j[1]:
                    tmp.append([m[1],m[2],m[3],m[4],m[5],m[6],m[7]])
            else:
                if flag==1:
                    break
        if tmp!=[]:
            tmp.sort(key=lambda x:x[0],reverse=False)
            totalTmp=[j[0],j[1]]
            for x in tmp:
                for a in x:
                    totalTmp.append(a)
            totalTmp.append(j[2])
            totalTmp.append(j[3])
            #print(totalTmp)
            if len(totalTmp)!=46:
                print(date)
                date = j[1]
                continue
            else:
                totalData.append(totalTmp)
        print(date)
        date = j[1]

print(totalData)

with open('monthFinalData.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in totalData:
        writer.writerow(row)
    f.close()
"""
"""
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
    """
"""
print(totalData)
"""
