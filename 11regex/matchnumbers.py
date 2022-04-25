import re

#怎么匹配出X-DSPAM里面的float，而不匹配后面的浮点数
str='X-DSPAM-Confidence: 451.632\n0.4589'
a=re.findall('^X\S+: ([0-9].+)',str)
print(a)
