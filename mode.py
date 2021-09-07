import csv 
from collections import Counter
with open('heightweight.csv', newline = '')as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(num)

data = Counter(newData)
modeData = {
   
    "75-85":0,
    "85-95":0
}
for height,occurence in data.items():
    if(50<float(height)<60):
        modeData["75-85"]+=occurence
    elif 60<float(height)<70:
        modeData["85-95"]+=occurence
    

modeRange,modeOccurence=0,0
for range,occurence in modeData.items():
    if occurence>modeOccurence:
        modeRange,modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0]+modeRange[1])/2)
print("the mode is:",mode)