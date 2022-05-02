import json

data='''
[
{
    "id":"001",
    "x":"2",
    "name":"Chuck"
},
{
    "id":"008",
    "x":"7",
    "name":"Brant"
}

]

'''

info=json.loads(data)
print('user count:',len(info))

for item in info:
    print('name=',item['name'])
    print('id=',item['id'])
    print('x=',item['x'])
