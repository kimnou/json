import json
print("Started Reading JSON file")
with open("load.json", "w") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    l=json.load(read_file)
    for key, value in l.items():
        print(key, ":", value)
    print("Done reading json file")