#From: stephen.marquard@uct.ac.za

import re

filehandle =open("mbox1.txt")

for line in filehandle:
    a=re.findall('From:.+@.+',line)

    if len(a)>0:
        print(a)
