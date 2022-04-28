import urllib.request
import re


#request

data=urllib.request.urlopen('https://www.baidu.com').read().decode()

#match

li=re.findall('href="(https?://.+?)"',data)

for i in li:
    print(i)
