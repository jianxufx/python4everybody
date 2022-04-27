
import re
hfile=open('mbox1.txt')

mydata=hfile.read()


a=re.findall('\S+@\S+',mydata)

for address in a:
    print(address)
