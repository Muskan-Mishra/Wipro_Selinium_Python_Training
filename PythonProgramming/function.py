from os.path import isdevdrive


def squ(x):
    result=x*x
    return result


print("square", squ(3))

def func_pass():
    pass
func_pass()


#multiple function cll
def cal(a,b):
    return a+b, a-b, a*b

add ,sub, mul = cal(10 , 2)
print(add)
print(sub)
print(mul)

#function calling a another function

def areaofrect(len,width):
    return len*width

def areaofsq(sq):
    return sq*sq

value = areaofrect(4,6)
sqr = areaofsq(value)
print(value)
print(sqr)

#function with a loop

def even(limit):
    for i in range(2, limit+1, 2):
        print(i)
even(10)

#function with condition

def even(limit):
    if limit%2 == 0:
        return "even"
    else:
        return "odd"
print(even(10))
print(even(11))






