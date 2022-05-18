import json
x={"name":"John","age":30,"children":("Ann","Billy")}
print(json.dumps(x, separators=(".", " = ")))