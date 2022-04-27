
import re


a='aabbccjfjsdjflsjflscc'
p1=re.findall('aa.+cc',a)
print(p1)
p2=re.findall('aa.+?cc',a)
print(p2)
