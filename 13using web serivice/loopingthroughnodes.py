import xml.etree.ElementTree as ET

input ='''

<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
  <name>Jim</name>
  <user>abc</user>
  <user>def</user>
</stuff>
'''

tree=ET.fromstring(input)
users=tree.find('users/user')
print(users.find('id').text)



for item in users:
    print(item.find('id').text,item.find('name').text,item.get('x'))
