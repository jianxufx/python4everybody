from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url='https://assignmentsbag.com/assignments-for-class-12-english/'
html=urllib.request.urlopen(url,context=ctx).read()


url=[]
name=[]
soup=BeautifulSoup(html,'html.parser')







'''
for i in a:
    href=str(i['href'])
    content=str([i.contens])
    if href.startswith('https://drive.google.com/uc'):
        url.append(href)
        name.append(content)
'''
