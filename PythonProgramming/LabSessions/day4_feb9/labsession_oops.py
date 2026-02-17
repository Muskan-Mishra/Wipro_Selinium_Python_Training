import math

from PythonProgramming.LabSessions.day3_feb7.labsession_module import length

#1
class Book:
    def __init__(self , tittle , author):
        self.tittle = tittle
        self. author = author
    def display(self):
        print(self.tittle, self.author)
b1 = Book("the god of small things" , "arundhati roy")
b2 = Book("midnight children" , " salman")
b3 = Book("the white tiger", "arviand")
b1.display()
b2.display()
b3.display()
#2
class rectangle:
    def __init__(self , length , width) :
        self.length = length
        self.width = width

        self.area = length *width
        self. perimeter = 2 *(length + width)
    def display(self):
        print( self.area, self.perimeter)

rec = rectangle(3,5)
rec.display()

#3 single level inherit

class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Balance:", self.balance)

class InterestAccount(SavingsAccount):
    def addinterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest Added:", interest)
        print("Balance:", self.balance)

obj = InterestAccount(1000)
obj.deposit(500)
obj.addinterest(5)

#1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
import math
class circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        r = math.pi * self.radius * self.radius
        print(r)


    def perimeters(self):
        t = 2 * math.pi * self.radius
        print(t)

c = circle(5)
c.area()
c.perimeters()

#22.Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import  date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # format: (year, month, day)

    def age(self):
        today = date.today()
        birth_date = date(self.dob[0], self.dob[1], self.dob[2])
        a = today.year - birth_date.year
        print(a)


p = Person("Muskan", "India", (2003, 5, 10))
p.age()

#3.Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        a= math.pi * self.r * self.r
        print(a)

    def perimeter(self):
        p = 2 * math.pi * self.r
        print(p)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        a= self.side * self.side
        print(a)

    def perimeter(self):
        p = 4 * self.side
        print(p)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        a = self.a + self.b + self.c
        print(a)


    def area(self):
        s = self.perimeter() / 2
        p = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(p)


sq = Square(4)
sq.area()
sq.perimeter()
cr = circle(5)
cr.area()
cr.perimeters()
#tr = Triangle(3,5,9)
#tr.area()
#tr.perimeter()

#4Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def show(self):
        print("Vehicle Name:", self.name)
        print("Speed:", self.speed)


class Bus(Vehicle):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity

    def display(self):
        self.show()
        print("Capacity:", self.capacity)


b = Bus("School Bus", 60, 40)
b.display()

#5Vehicle class without variables and methods
class vehicle:
    pass

