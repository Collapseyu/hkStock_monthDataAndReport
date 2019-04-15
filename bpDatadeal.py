import csv
import re
csv_file=csv.reader(open('monthFinalDataWithPrice.csv','r'))
data=[]
for i in csv_file:
    tmp=[]
    for j in i:
        tmp.append(j)
    data.append(tmp)
print(data)
bpData=[]
#rst_third = re.findall((r"['](.*?)[']"), data[0][0])
#tmpData=re.findall(r"['](.*?)[']",data[266][1])
#if tmpData[4]=='':
#   print(tmpData)
#tmpLastD=re.findall(r"['](.*?)[']",i[j-1])
"""
for i in data:
    for j in range(1,len(i)):
        #tmp=[i[j][0],i[j][1],float(i[j][2]),float(i[j][3]),float(i[j][4]),float(i[j][5])-float(i[j-1][5]),float(i[j][6])-float(i[j-1][6]),float(i[j][7])-float(i[j-1][7])]
        tmpData=re.findall(r"['](.*?)[']",i[j])
        tmpLastD=re.findall(r"['](.*?)[']",i[j-1])
        if tmpData[2]=='' or tmpData[3]=='' or tmpData[4]=='' or tmpData[5]=='' or tmpData[7]=='' or tmpData[7]=='':
            continue
        if tmpLastD[2]=='' or tmpLastD[3]=='' or tmpLastD[4]=='' or tmpLastD[5]=='' or tmpLastD[7]=='' or tmpLastD[7]=='':
            continue
        tmp=[tmpData[0],tmpData[1],float(tmpData[2]),float(tmpData[3]),float(tmpData[4]),float(tmpData[5])-float(tmpLastD[5]),float(tmpData[6])-float(tmpLastD[6]),float(tmpData[7])-float(tmpLastD[7])]
        bpData.append(tmp)
        print(tmp)
"""
for i in data:
    if(len(i)!=6):
        continue
    for j in i:
        tmpData=re.findall(r"['](.*?)[']",j)
        if tmpData[3] == '' or tmpData[4] == '' or tmpData[5] == '' or tmpData[6] == '' or tmpData[7] == '' or tmpData[8] == ''or tmpData[10] == ''or tmpData[11] == ''or tmpData[12] == '' or tmpData[13] == '' or tmpData[14] == '' or tmpData[15] == '' or tmpData[17] == '' or tmpData[18] == '' or tmpData[19] == ''or tmpData[20] == '' or tmpData[21] == '' or tmpData[22] == '' or tmpData[24] == ''or tmpData[25] == '' or tmpData[26] == '' or tmpData[27] == '' or tmpData[28] == ''or tmpData[29] == '' or tmpData[31] == '' or tmpData[32] == '' or tmpData[33] == ''or tmpData[34] == '' or tmpData[35] == '' or tmpData[36] == '' or tmpData[38] == ''or tmpData[39] == '' or tmpData[40] == '' or tmpData[41] == '' or tmpData[42] == ''or tmpData[43] == '' or tmpData[44] == '' or tmpData[45] == '' or tmpData[46] == '':
            continue
        tmp=[tmpData[0],tmpData[1],float(tmpData[3]),float(tmpData[4]),float(tmpData[5]),float(tmpData[6]),float(tmpData[7]),float(tmpData[8]),float(tmpData[10]),float(tmpData[11]),float(tmpData[12]),float(tmpData[13]),float(tmpData[14]),float(tmpData[15]),float(tmpData[17]),float(tmpData[18]),float(tmpData[19]),float(tmpData[20]),float(tmpData[21]),float(tmpData[22]),float(tmpData[24]),float(tmpData[25]),float(tmpData[26]),float(tmpData[27]),float(tmpData[28]),float(tmpData[29]),float(tmpData[31]),float(tmpData[32]),float(tmpData[33]),float(tmpData[34]),float(tmpData[35]),float(tmpData[36]),float(tmpData[38]),float(tmpData[39]),float(tmpData[40]),float(tmpData[41]),float(tmpData[42]),float(tmpData[43]),float(tmpData[44]),float(tmpData[45]),float(tmpData[46])]
        bpData.append(tmp)
        print(tmp)

with open('monthlstmDataSet.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in bpData:
        writer.writerow(row)
    f.close()
