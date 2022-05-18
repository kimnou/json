import json
dic={}
a=open("meraki7.txt")
for i in a:
    key,value=i.strip().split(None,1)
    dic[key]=value.strip()
print(json.dumps(dic,indent=6))
f=open("meraki7.json","w")
json.dump(dic,f,indent=3)
f.close()


     
# a=[6,1,3,5,6,3,2]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)
# m=1
# l=len(b)
# for j in range(l-1):
#     m=m*b[j]
# print(m)