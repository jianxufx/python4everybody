import requests
import bs4
url='https://assignmentsbag.com/assignments-for-class-12-english/'
a=requests.get(url)

html=a.text
soup=bs4.BeautifulSoup(html,'html.parser')

a=soup.find_all(rel='profile')


print(a)
