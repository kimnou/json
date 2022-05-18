### Json data ko python object main convert karne ka program likho?.

import json
dict='{"name":"jen","profession":"doctor","age":36}'
d=json.loads(dict)
print(d)
print(d["name"])
print(d["age"])
print(d["profession"])
