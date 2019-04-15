import csv
import re
def quarterDataDeal(): #拼接带速动比率，流动比率的数据和每股基本收益
    csv_file = csv.reader(open('quarterFinalData.csv', 'r'))
    stock = []
    for i in csv_file:
        stock.append(i)
    del stock[0]
    print(stock)
    csv_file = csv.reader(open('eastReportPrice.csv', 'r'))
    price = []
    for i in csv_file:
        price.append(i)
    print(price)
    totalData =  [['股票编号','报告日期','日期','收盘价','涨跌幅','换手率','日期','收盘价','涨跌幅','换手率','基本每股收益','流动比率','速动比率']]
    order = []
    for i in price:
        flag = 0
        for j in stock:
            if j[0] == i[0]:
                flag = 1
                if j[1] == i[1]:
                    tmp = []
                    flagZ=0
                    for z in range(16):
                        if(z==0 or z==1 or z==2 or z==9):
                            tmp.append(j[z])
                        else:
                            if(j[z]==''):
                                flagZ=1
                                break
                            else:
                                tmp.append(j[z])
                        # tmp=[j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18],j[19],j[20],j[21],j[22],j[23],j[24],j[25],j[26],j[27],j[28],j[29],j[30],j[31],j[32],j[33],j[34],j[35],j[36],j[37],j[38],j[39],j[40],j[41],j[10],j[11],j[12],j[13],j[14],j[15],i[2],j[-2],j[-1]]
                    if flagZ==0:
                        tmp.append(i[2])
                        tmp.append(j[-2])
                        tmp.append(j[-1])
                        totalData.append(tmp)
            else:
                if flag == 1:
                    break
    csv_file = csv.reader(open('eastReportasset.csv', 'r'))
    asset = []
    for i in csv_file:
        asset.append(i)
    print(asset)
    totalData4=[]
    for i in asset:
        flag = 0
        for j in totalData:
            if j[0] == i[0]:
                flag = 1
                if j[1] == i[1]:
                    tmp = []
                    flagZ=0
                    for z in range(16):
                        if(z==0 or z==1 or z==2 or z==9):
                            tmp.append(j[z])
                        else:
                            if(j[z]==''):
                                flagZ=1
                                break
                            else:
                                tmp.append(j[z])
                        # tmp=[j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18],j[19],j[20],j[21],j[22],j[23],j[24],j[25],j[26],j[27],j[28],j[29],j[30],j[31],j[32],j[33],j[34],j[35],j[36],j[37],j[38],j[39],j[40],j[41],j[10],j[11],j[12],j[13],j[14],j[15],i[2],j[-2],j[-1]]
                    if flagZ==0:
                        tmp.append(i[2])
                        tmp.append(i[3])
                        tmp.append(j[-3])
                        tmp.append(j[-2])
                        tmp.append(j[-1])
                        totalData4.append(tmp)
            else:
                if flag == 1:
                    break

    print(totalData)
    totalData2 = totalData4
    totalData3 = []
    tmp = []
    del totalData2[0]
    last = totalData2[0][0]
    for i in totalData2:
        if i[0] != last:
            totalData3.append(tmp)
            last = i[0]
            tmp = []
            tmp.append(i)
        else:
            tmp.append(i)
    print(totalData3)
    for i in totalData3:
        i.sort(key=lambda x: x[1], reverse=False)
    print(totalData3)
    for i in totalData3:
        order.append(i[0][0])
    print(order)
    return totalData3,order
def bpDataset():
    csv_file = csv.reader(open('quarterFinalDataWithPriceandAsset.csv', 'r'))
    data = []
    for i in csv_file:
        tmp=[]
        for j in i:
            tmp.append(j)
        data.append(tmp)
    print(data)
    bpData = []
    for i in data:
        for j in range(1, len(i)):
            # tmp=[i[j][0],i[j][1],float(i[j][2]),float(i[j][3]),float(i[j][4]),float(i[j][5])-float(i[j-1][5]),float(i[j][6])-float(i[j-1][6]),float(i[j][7])-float(i[j-1][7])]
            tmpData = re.findall(r"['](.*?)[']", i[j])
            tmpLastD = re.findall(r"['](.*?)[']", i[j - 1])
            if tmpData[3] == '' or tmpData[4] == '' or tmpData[5] == '' or tmpData[6] == '' or tmpData[7] == '' or \
                    tmpData[8] == '' or tmpData[10] == ''or tmpData[11] == ''or tmpData[12] == ''or tmpData[13] == ''\
                    or tmpData[14] == ''or tmpData[15] == ''or tmpData[18] == '' or tmpData[19] == ''or tmpData[20] == '':
                continue
            if tmpLastD[16] == '' or tmpLastD[17] == '':
                continue
            tmp=[tmpData[0],tmpData[1]]
            for z in range(3,len(tmpData)-5):
                if z==9:
                    continue
                tmp.append(float(tmpData[z]))
            tmp.append(tmpLastD[16])
            tmp.append(tmpLastD[17])
            tmp.append(tmpData[18])
            tmp.append(tmpData[19])
            tmp.append(tmpData[20])
            bpData.append(tmp)
            print(tmp)
    return bpData
bpData=bpDataset()
#totalData,order=quarterDataDeal()

with open('quarterFinalDataBpDataSet1.0.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in bpData:
        writer.writerow(row)
    f.close()
"""
with open('quarterFinalOrderwithPriceandAsset.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in order:
        writer.writerow(row)
    f.close()
"""
