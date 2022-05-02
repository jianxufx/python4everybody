import json
import requests
data='''[

{"message":"https:\/\/images.dog.ceo\/breeds\/hound-basset\/n02088238_11635.jpg","status":"success"}

]'''


a=json.loads('''https://api.agify.io?name=michael)



print(a[0]['age'])
