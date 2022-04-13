a={'of':3,'is':8,'was':5,'the':1}

for key,value in a.items():
    print(key,value)


print('-'*20)

li=[]

for key,value in a.items():
    li.append((value,key))

li.sort(reverse=True)


for i,k in li:
    print(i,k)
