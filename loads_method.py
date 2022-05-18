import json

JsonString='''{"name":"jane","salary":9000,"skills":["pi","Web Development"],
"email": "JaneDoe@pynative.com"}'''
Dict=json.loads(JsonString)
print(Dict["name"])
print(Dict["skills"])
print(Dict["salary"])
print(Dict["email"])
