'''
https://assignmentsbag.com/assignments-for-class-12-english/
'''

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('assignmentsbag.com',443))

cmd='GET https://assignmentsbag.com/assignments-for-class-12-english/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


filehandle =open('testdrive.htm','wb+')

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

filehandle.close()
mysock.close()
