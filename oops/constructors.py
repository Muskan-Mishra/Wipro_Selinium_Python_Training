class Student:
    def __init__(self):
        print("contructor is called")

    def addsum(self):
        print("adding two numbers")


s1 = Student()
s1.addsum()

#parametrized constructor

class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, self.salary)
e1 = Employee("muskan" , 400000)
e2 = Employee("vishnu" , 50000)

e1.display()
e2.display()

#using * args in constuctor
class numbers:
    def __init__(self , *args):
        self.values = args
n = numbers(10 ,30, 56)
print(n.values)

m = numbers(3 ,8)
print(m.values)

p = numbers(3)
print(p.values)

# parent and child constructors
# super keyword  for accessing parent constructor
class parent:
    def __init__(self):
        print("i am the parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("i am the child constructor")
c = child()




