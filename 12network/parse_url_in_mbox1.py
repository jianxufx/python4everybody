import re

hfile=open('mbox1.txt')

data=hfile.read()

li=re.findall('https?://.+',data)

print(id(li[0]))

for item in li:
    print(id(item))
    index=item.find(')')
    item=item[:index-1]
    print(id(item))
    print(item)
    a=input()


print(li)




'''
for i in range(len(li)):
    index=li[i].find(')')
    li[i]=li[i][:index-1]




for i in li:
    print(i)
    a=input()
'''
