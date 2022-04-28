import urllib.request

website=urllib.request.urlopen('https://www.163.com').read()


hfile=open('163.html','wb')
hfile.write(website)
hfile.close()
