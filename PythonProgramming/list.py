empty_list = []
numbers = [1,2,3,4]
mixeddata = [1, "hello", True, 6.67, 1]
nested = [[1,2] , [3,4]]

#accessing the list elements (indexing concept)
print(mixeddata[1])
print(mixeddata[2])

#modifying the list
mixeddata[4] = 6
print(mixeddata)
# add elements # insert at index
#mixeddata.insert(__index:0, __object:10)
#print(mixeddata)
mixeddata.append("john")
print(mixeddata)
mixeddata.remove("hello")
print(mixeddata)
mixeddata.pop()
print(mixeddata)
mixeddata.pop(1)
print(mixeddata)


# list methods
print(numbers.sort())
print(numbers.reverse())
print(numbers.count(3))
print(numbers.index(3))
numbers.clear()
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)
for i, fruit in enumerate(fruits):
    print(i,fruit)

#slicing
my_list = ['p', 'r', 'o', 'g', 'r' , 'a', 'm']
print("my_list =", my_list)
print(my_list[2: 5])

print(my_list[5: ])

print(my_list[:])
a = [1, 2, 2, 3]
print(len(a))

# extends
numbers = [1, 3, 5]
even_numbers = [2, 4, 6]
numbers.extend(even_numbers)
print(numbers)
