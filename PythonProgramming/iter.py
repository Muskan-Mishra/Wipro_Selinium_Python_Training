a = [10,20,30,40,50]
#convert the list into  iterator
iterator =iter(a)
#next () allow the user to access the elements
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the string to  iterator
s = "hello"
iterator = iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the dict into iterator
d = {'a':1, 'b':2, 'c':3}
iterator = iter(d)
print(next(iterator))
print(next(iterator))

# for loop to iterate
for key in iterator:
    print(key)
d = {'a':1, 'b':2, 'c':3}
for key, value in d.items():
    print(key, "->" , value)

#iter(callable , sentinel)

def get_input():
    return input("enter value:")
for value in iter(get_input, "quit"):
    print("you entered:" , value)
print("loop ended")



