#parent class
class employee:
    def __init__(self , name , empid):
        self.name=name
        self.empid=empid

    def detail(self):
        print(self.name,self.empid)

#child class
class manager(employee):
    def approve_leave(self):
        print("leave approved")

m = manager("vishnu" , 40)
m.detail() #parent class
m.approve_leave() #from child class
