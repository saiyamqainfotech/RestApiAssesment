import requests 
import json

url = 'https://code-riddler.herokuapp.com/api/v1/candidates/'

mydata = {
    "username": "saiyamarora",
    "password": "password",
    "first_name": "Saiyam",
    "last_name": "Arora",
    "email": "saiyamarora@qainfotech.com"
}

r = requests.post(url,data = mydata)
check_id = r.content 
print(check_id)
