import urllib.request

file_data=urllib.request.urlopen('http://data.pr4e.org/mbox.txt')

filehandle=open('mbox.txt','wb+')

while True:
    data=file_data.read(512)
    if len(data)<1:
        break
    filehandle.write(data)

filehandle.close()
