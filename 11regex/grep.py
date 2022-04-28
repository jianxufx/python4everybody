import re
rule=input('please enter a reglular expression:\n')

hfile =open('mbox.txt')
count=0
for line in hfile:
    data=re.findall(rule,line)
    if data:
        count=count+1


print(count)
