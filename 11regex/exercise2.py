import re

hfile =open('mbox.txt')

count_line=0
sum=0
data=[]

#New Revision: 39772
for line in hfile:
    data=re.findall('New Revision: ([0-9]*)',line)
    if data:
        count_line=count_line+1
        sum=sum+int(data[0])

print("count_line=",count_line,'sum=',sum,'average=',round(sum/count_line,2))
