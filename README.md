# Municipalities-and-Province

import requests

request_api = requests.post("https://sfrs-j75dy.ondigitalocean.app/api/listDistricts")
#print(request_api.status_code)
#print(request_api.json())

i=0

print ("{:<40} {:<30}".format('Municipalities','Province'))

for i in range(0,11):
    municipalities=request_api.json()['data'][int(i)]['name']
    province=request_api.json()['data'][int(i)]['province']['name']
    municipalities+=" District"
    print ("{:<40} {:<30}".format(municipalities,province))
    i+=1
    municipalities=""
