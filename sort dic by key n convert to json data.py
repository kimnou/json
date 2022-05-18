## write a program to convert python dictionay,(sorted by key)
## to json data

import json
a={'4':5,'6':7,'1':3,'2':4}
b=sorted(a.values())
c={}
for i in b:
    for j in a:
        if a[j]==i:
            c[j]=i
x=json.dumps(c)      
print(x)
