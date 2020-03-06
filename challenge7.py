import requests 
import json 


url1 = 'https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/' 

username = "saiyamarora"
password = "password"

auth_u = (username, password)
r = requests.get(url=url1, auth=auth_u)
txt = r.json()
print(txt)

dict = json.loads(r.text)
myDict = dict.get('test_input')
myValue = myDict.get('list')
inp = []

inp = myValue.strip('[]').split(", ")

lt = []
for i in inp:
    if(i not in lt):
        lt.append(i)
print(lt)


headers={'Content-type':'application/json', 'Accept':'application/json'}
url2= 'https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/'
myOut = {
    "test_session": 12,  
    "output": {'list': lt},     
    "challenge": 5   
     }


rout = requests.post(url = url2, data = json.dumps(myOut), auth = (username,password), headers = headers)
print(rout.status_code)
print(rout.text)