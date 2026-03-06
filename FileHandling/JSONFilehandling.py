import json
with open("/dataformats//employee.json", 'r') as file:
    data = json.load(file)
#read load method
print(data)

print(data["name"])

with open("/dataformats//nestedjson.json", 'r') as file:
    data = json.load(file)
email = data["user"]["profile"]["email"]
print(email)



# update or modify the json file
#read the  json file
#modify the data
#write it back to the file
with open("/dataformats//updatejson.json", 'r') as file:
    data = json.load(file)

data["experience"] = 6

with open("/dataformats//updatejson.json", 'w') as file:
    json.dump(data, file, indent = 4)
