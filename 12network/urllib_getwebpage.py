import urllib.request
import ssl
import re


#no ssl certifaction alert
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#get all the google drive link
htm=urllib.request.urlopen('https://assignmentsbag.com/assignments-for-class-12-english/',context=ctx).read().decode()
#urlopen是同步操作，直到完成请求才会执行后面的代码

#get link list
urllist=re.findall('<a href="(https://drive.google.com/.*?)"',htm)
#get name list
filename=re.findall('<a href="https://drive.google.com/.*?">(.*?)</a>',htm)


def myunescape_decode(li):
    #maketrans替换功能 参数长度必须相同，a->b 不能abc->d

    map=[('%3A',':'),('%2F','/'),('%3F','?'),('%3D','='),('%26','&'),('amp;','')]

    for i in range(len(li)):
        url=li[i]
        for item in map:
            (a,b)=item
            url=url.replace(a,b)
        li[i]=url



myunescape_decode(urllist)
myunescape_decode(filename)

link_dict=dict()

for i in range(len(urllist)):
    link_dict[filename[i]]=urllist[i]


print(link_dict)
