import csv
csv_file=csv.reader(open('Train.csv','r'))
xData=[]
yData=[]
for i in csv_file:
    xData.append(i[:3])
    yData.append(i[3:])
print(xData)
print(yData)
"""
trainSet=[]
testSet=[]
n=0
for i in csv_file:
    if n<4000:
        trainSet.append(i)
    if n>=4000 and n<5000:
        testSet.append(i)
    n+=1
print(len(testSet))
with open('Train.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in trainSet:
        writer.writerow(row[2:])
    f.close()
with open('Test.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in testSet:
        writer.writerow(row[2:])
    f.close()
"""