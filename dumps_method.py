import json
a={"lalala":3}
b=json.dumps(a)
c=json.dumps(a,indent=0)
d=json.dumps(a,indent=4)
print(b)
print(c)
print(d)