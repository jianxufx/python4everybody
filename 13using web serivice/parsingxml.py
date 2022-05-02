import xml.etree.ElementTree as ET

data='''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
'''

a=ET.fromstring(data)
print(a.find('name').text)
