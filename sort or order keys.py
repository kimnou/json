import json

x={"name":"John","age":30,"married":True,"divorced":False,"pets":None}
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))