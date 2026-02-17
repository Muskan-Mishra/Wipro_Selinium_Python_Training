#paramerzired with multiple methods
class calculator:
    def add(self , a, b):
        print(a+b)
c = calculator()
c.add(3,4)
c.add(6,9)
 # default parameters
class test:
     def run(self, browser = "chrome"):
         print("running on ", browser)

t = test()
t.run()
t.run("firefox")

#*args parameter methods
class numbers:
    def total(self,*args):
        print(sum(args))
n = numbers()
n.total(3,5,6)
n.total(6,9)
n.total(7)