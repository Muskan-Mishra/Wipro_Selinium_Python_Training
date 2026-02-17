# Create a dictionary with roll number as key and name as value
students = {
    101: "Amit",
    102: "Neha",
    103: "Rahul",
    104: "Priya"
}

# Print the dictionary
print("Dictionary:", students)

# Access the value of an existing key
print("Value for key 102:", students[102])

# Access the value of a key that does NOT exist (using get to avoid error)
print("Value for key 110:", students.get(110, "Key does not exist"))

# Update the value of an existing key
students[103] = "Rohit"
print("After updating key 103:", students)

# Delete a key using del
del students[104]
print("After deleting key 104 using del:", students)

# Delete a key using pop()
students.pop(101)
print("After deleting key 101 using pop():", students)

# Find the number of key-value pairs
print("Number of key-value pairs:", len(students))

# Print only keys
print("Keys:", students.keys())

# Print only values
print("Values:", students.values())

# Print key-value pairs
print("Key-Value pairs:", students.items())


# Python script to concatenate dictionaries to create a new one

# Dictionaries
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
dict3 = {'e': 50}

# Concatenation
new_dict = {}
for d in (dict1, dict2, dict3):
    new_dict.update(d)

print(new_dict)