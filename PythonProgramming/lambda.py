#normal fun of adding 2 no
from functools import reduce


def add(a,b):
    return a+b
print(add(5 ,3))

#lambda fun
add = lambda a,b: a+b
print(add(5 ,3))
#square of a number
square = lambda x: x*x
print (square(5))
# even no
even = lambda x: x%2 == 0
print(even(4))

#find max of two no
max = lambda a,b : a if a > b else b
print(max(10,30))

#filter
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens)

#filter the failed testcase
status = ['pass', 'fail', 'pass', 'fail']
failed = list(filter(lambda s:s == 'fail', status))
print(failed)

#positive
nums = [-5, 10, -3, 7, 0, 2]
positive = list(filter(lambda s:s > 0,nums))
print(positive)
#Filter non-empty strings
data = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda d: d!="", data))
print(non_empty)

#reduce
#from functools import reduce
nums = [10,20,30,40]
print(reduce(lambda x ,y : x+y , nums))
#multiply
print(reduce(lambda x,y: x*y, nums))
#maximum
print(reduce(lambda x,y: max(x,y), nums))
#minimum
print(reduce(lambda x,y: min(x,y), nums))

#map
nums = [10,20,30,40]

squares = list(map(lambda x : x*x , nums))
print(squares)

data = [(1,3),(4,1),(2,2)]
sorteddata = sorted(data , key = lambda x : x[0])
print(sorteddata)

marks = {"a": 75, "b":90, "c":60}
sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_marks)

print(list(map(lambda x: x+x,[1,2,3])))
print(list(filter(lambda x: x, [0, 1, False, True, 2])))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 2))
print(list(filter(lambda x: x > 2, map(lambda x: x + 1, [1, 2, 3]))))
print(list(map(lambda x: x.upper(), filter(lambda x: x.islower(), "PyThOn"))))
print(list(map(lambda x: x[0], ["python", "java", "c++"])))
f = map(lambda x: x * 2, nums)
nums.append(4)
print(list(f))
nums = [1, 2, 3]
f = map(lambda x: x * 2, nums)
nums.append(4)
print(list(f))
print(list(filter(None, [0, "", None, 5, "Hi"])))