'''
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



'''
a=[1,3,5,10,9]

def test(li):
    b=[]

    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])
    return b

b=[]
def test2(li,b):
    b.append(li[i])
