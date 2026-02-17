#dictionary items - key value
country = {
    "India":"delhi",
    "canada":"ottawa",
    "england":"london"
}
print(country)
#access the values with the keys
print(country["canada"])

#add elements
country["Italy"] = "Rome"
print(country)

#remove elements
del country["India"]
print(country)
#clear
#country.clear()
#print(country)
#iterate among the dict
for coun in country:
    print(coun)

#lenghth of the dict
print(len(country))



#for integers tuples are string - keys nust be immutable
#integer is a key

my_dict = {1:"one" , 2:"two" , 3:"three" }
print(my_dict)

mt_dict = {1:"one" , 2:"two" , 3:"three" , 1:"one"}
print(my_dict)

#integer key must be immutable

#tuple as akey
my_dict = {(1,2):"one two" , 3:"three"}
print(my_dict)

my_dict = {(1,2):"one two" , 3:"three" , 3:"four"}
print(my_dict)


#pop - removes the item with spec key
my_dict = {'a':1 , 'b':2 , 'c':3}
removed_value = my_dict.pop('b')
print(removed_value)
print(my_dict)


#update() _ adds or changes the dict
my_dict = {"brand":"ford", "model":"mustang" , "color":"red" }
my_dict["color"] = "green"
print(my_dict)


#key()

#values()
#popitem() return the last
my_dict = {
    'apple':1,
    'banana':2,
    'orange':3
}
last_item = my_dict.popitem()
print(last_item)
print(my_dict)

#dict inside the list
employee = [
    {"id":1, "name":"muskan", "role":"qa"},
    {"id":2, "name":"riya", "role":"dev"},
    {"id":3, "name":"sanju", "role":"manger"}

]
print(employee[0])
print(employee[0]["name"])
for emp in employee:
    print(emp["name"],emp["role"])
employee.append({"id":4 ,"name":"sita", "role":"tester"})
print(emp)
employee.pop(0)
print(employee)

for emp in employee:
    if emp["name"]== "muskan":
        print(emp)











