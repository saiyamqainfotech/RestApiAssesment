import requests
import json
import urllib

url = 'https://code-riddler.herokuapp.com/api/v1/testsessions/'
mydata = { "candidate": 76 }
username = "saiyamarora"
password = "password"
auth_u = (username,password)
r = requests.post(url,data=mydata, auth=auth_u)
check_Id = r.content
check_status = r.status_code
print(check_Id)
print(check_status)