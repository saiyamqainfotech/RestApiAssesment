import requests 
import json 


url1 = 'https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/' 

username = "saiyamarora"
password = "password"

auth_u = (username, password)
r = requests.get(url=url1, auth=auth_u)
txt = r.text
print(r.status_code)
print(txt)

dict = json.loads(r.text)
myDict = dict.get('test_input')
myValue = myDict.get('text')


inp = myValue
count = 0
for i in inp:
    if(i!=' '):
        if(i!='.'):
            if(i!='\n'):
                count += 1
print(count)


headers={'Content-type':'application/json', 'Accept':'application/json'}
url2= 'https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/'
myOut = {
    "test_session": 12,  
    "output":{"count": 367},     
    "challenge": 1    
     }
print(myOut)

rout = requests.post(url = url2, data = json.dumps(myOut), auth = (username,password), headers = headers)
print(rout.status_code)
# print(rout.content)
print(rout.text)
