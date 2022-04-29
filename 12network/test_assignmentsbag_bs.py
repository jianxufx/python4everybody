import urllib.request
from bs4 import BeautifulSoup


website=urllib.request.urlopen('https://assignmentsbag.com/assignments-for-class-12-english/').read()

soup=BeautifulSoup(website,'html.parser')

li_url=[]
li_name=[]
urls=soup.find_all('a')

for i  in  urls:
    if str(i.get('href')).startswith('https://drive.google'):
        li_url.append(str(i.get('href')))
        li_name.append(str(i.string))


for i  in  range(len(li_url)):
    print(li_url[i],li_name[i])
