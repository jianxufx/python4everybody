import re

hfile=open('test.html')

li=[]

for line in hfile:
    href=re.findall('href="(https?://.+)"',line)
    if len(href)<1:
        continue
    li=li+href
print(li)
