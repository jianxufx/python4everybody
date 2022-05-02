import urllib.request
from bs4 import BeautifulSoup
import os
import time
import ssl

#no ssl certifaction alert
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


website=urllib.request.urlopen('https://assignmentsbag.com/assignments-for-class-12-english/').read()

soup=BeautifulSoup(website,'html.parser')

li_url=[]
li_name=[]
urls=soup.find_all('a')

for i  in  urls:
    if str(i.get('href')).startswith('https://drive.google'):
        li_url.append(str(i.get('href')))
        li_name.append(str(i.string))



folder='mydownload_3.1415926'

try:
    os.makedir(folder)
except:
    print('folder exist')
    pass

#set current working dictory
currentpath=os.chdir(os.getcwd()+'\\'+folder+'\\')


for i in  range(len(li_url)):

    print(li_name[i],'start to download!\n')

    data=urllib.request.urlopen(li_url[i],context=ctx).read()

    time.sleep(5)

    path=li_name[i]+'.pdf'

    hfile=open(path,'wb')
    hfile.write(data)
    hfile.close()

    print(li_name[i],'downloading compeleted!\n')

print('mission compeleted!')
