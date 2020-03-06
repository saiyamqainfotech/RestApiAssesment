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
inp = inp.lower()
vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
for i in inp:
    if(i=="a"):
        vowels["a"] +=1
    elif(i=="e"):
        vowels["e"] += 1
    elif(i=="i"):
        vowels["i"] += 1
    elif(i=="o"):
        vowels["o"] += 1
    elif(i=="u"):
        vowels["u"] += 1

headers={'Content-type':'application/json', 'Accept':'application/json'}
url2= 'https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/'
myOut = {
    "test_session": 12,  
    "output": vowels,     
    "challenge": 4    
     }
print(myOut)

rout = requests.post(url = url2, data = json.dumps(myOut), auth = (username,password), headers = headers)
print(rout.status_code)
# print(rout.content)
print(rout.text)