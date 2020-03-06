import requests 
import json 
import ast

url1 = 'https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/' 

username = "saiyamarora"
password = "password"

auth_u = (username, password)
r = requests.get(url=url1, auth=auth_u)
txt = r.text
print(r.status_code)
print(txt)

# final = r.json()

# final = r.json()
print("f###")
# final1 = ['test_input'][]
# print(final1)

dict = json.loads(r.text)
myDict = dict.get('test_input')
myValue = myDict.get('list')
data3 = myValue
data4 = ast.literal_eval(data3)
#############
myplayer = data4.get('player1')
#print(myplayer)
myplayer2 = data4.get('player2')
#print(myplayer2)



SP = 100
CL = 50
HT = -100
DD = -50

print("sdfyft")
print(myplayer[0][1])
def poker(player):
    ll = []
    pot = 1000
    for i in range(len(player)):
        # print(myplayer[i][0])
        # print(myplayer[i][1])
        if player[i][0] == 'SP':
            pot +=100
        if player[i][0] =='CL':
            pot += 50
        if player[i][0] =='HT':
            pot -= 100
        if player[i][0] =='DD':
            pot -= 50
        if player[i][1] == 'SP':
            pot +=100
        if player[i][1] =='CL':
            pot += 50
        if player[i][1] =='HT':
            pot -= 100
        if player[i][1] =='DD':
            pot -= 50
        # ll.append(pot)
    return pot

ans = ""

if(poker(myplayer) < poker(myplayer2)):
    ans = "player2"
else:
    ans = "player1"


print(ans)
headers={'Content-type':'application/json', 'Accept':'application/json'}
url2= 'https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/'
myOut = {
    "test_session": 12,  
    "output": {"winner": ans },     
    "challenge": 7    
     }
print(myOut)
rout = requests.post(url = url2, data = json.dumps(myOut), auth = (username,password), headers = headers)
print(rout.status_code)
# print(rout.content)
print(rout.text)
