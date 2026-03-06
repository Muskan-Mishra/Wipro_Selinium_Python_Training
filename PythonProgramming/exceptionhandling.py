#custom exception
try:
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("please enter valid numbers")

#genric exception
try:
    a = 10/2
except Exception as e:
    print(e)
else:
    print("division successfull")

finally:
    print("close the browser")

#custom exception
age = int(input("enter the age"))
if age < 18:
    raise ValueError("age must be 18 or above")