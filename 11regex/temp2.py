import re

line='Hello World\n'


res=re.findall('(H..).(o..)',line)
print(res)
