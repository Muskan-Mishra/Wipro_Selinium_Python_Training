print (len("python"))# string
print (len([1, 2, 3]))#list
print (len({1, 2, 3}))# set


class calculator:
    def add(self, a,b=0, c=0):
        return a+b+c
c = calculator()
print(c.add(5))
print(c.add(3,5))
print(c.add(3,5, 8))

class animal:
    def sound(self):
        print("animals make sound")

class dog(animal):
    def sound(self):
        print("dog barks")
a = animal()
c = dog()
a.sound()
c.sound()



