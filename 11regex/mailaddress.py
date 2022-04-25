import re

del_char=";><'"

filehandle =open('mbox1.txt')

for line in filehandle:
    if line.startswith('From: '):

        a=re.findall('[a-zA-z0-9]+@[a-zA-z0-9]+',line)

        if len(a)>0:
            print(a)
