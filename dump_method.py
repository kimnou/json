import json

dict={"name":"Lisa","designation":"programmer","age":"34","salary":"54000"}
out_file=open("myfile.json","w")
json.dump(dict,out_file)
out_file.close()


# dict={"name":"sam","rollno":56,"cgpa":8.6,"PhNo.":"9976770500"}
# with open("sample.json", "w") as outfile:
#     json.dump(dict,outfile)