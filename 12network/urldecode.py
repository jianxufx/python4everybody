import re
url='https%3A%2F%2Fdrive.google.com%2Fuc%3Fexport%3Ddownload%26id%3D1wyfexigemiymmfu5i4_yeo1pitvyudqp'


# %3a->: %2f->/
#chr(3a)
'''
string.maketrans('%3a',':')
                 %2f    /
                 %3f    ?
                 %3d    =
                 %26    &

'''
li=[('%3A',':'),('%2F','/'),('%3F','?'),('%3D','='),('%26','&')]

for item in li:
    (a,b)=item
    url=url.replace(a,b)
