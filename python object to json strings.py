import json

# a={"day":'saturday',"date":17,"month":'jan',"year":2022}
# file1=open("meraki3.json","w")
# json.dump(a,file1,indent=4)
# file1.close


a={"day":'saturday',"date":17,"month":'jan',"year":2022}
with open("meraki33.json","w") as file1:
    json.dump(a,file1,indent=4)
