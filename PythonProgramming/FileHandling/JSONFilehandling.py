import json
with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//employee.json" , 'r') as file:
    data = json.load(file)
#read load method
print(data)

print(data["name"])

with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//nestedjson.json" , 'r') as file:
    data = json.load(file)
email = data["user"]["profile"]["email"]
print(email)



# update or modify the json file
#read the  json file
#modify the data
#write it back to the file
with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//updatejson.json" , 'r') as file:
    data = json.load(file)

data["experience"] = 6

with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//updatejson.json" , 'w') as file:
    json.dump(data, file, indent = 4)
