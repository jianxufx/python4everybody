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


link_dict=dict()

#get link list
urllist=re.findall('<a href="(https://drive.google.com/.*?)"',htm)
#get name list
rawfilename=re.findall('<a href="https://drive.google.com/.*?">(.*?)</a>',htm)

#link  filename 需要upescape 和decoder

print(urllist)
print('\n')




def myunescape_decode(urllist):
    #maketrans替换功能 参数长度必须相同，a->b 不能abc->d

    map=[('%3A',':'),('%2F','/'),('%3F','?'),('%3D','='),('%26','&'),('amp;','')]

    for i in range(len(urllist)):
        url=urllist[i]
        for item in map:
            (a,b)=item
            url=url.replace(a,b)
        urllist[i]=url



myunescape_decode(urllist)

print(urllist)
