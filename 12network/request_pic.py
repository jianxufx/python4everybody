import socket
import re


mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('piketty.pse.ens.fr',80))

cmd='GET http://piketty.pse.ens.fr/files/0-19-928688-4_chap00.pdf HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


filehandle =open('0-19-928688-4_chap00.pdf','wb+')


#find header
header=mysock.recv(512)
index=header.find(b'\r\n\r\n')
#find the start point  of the body in the first recv data
partbody=header[index+4:]
#write
filehandle.write(partbody)


#request the rest of the body
while True:
    data=mysock.recv(512)
    if(len(data)<1):
        break
    filehandle.write(data)
