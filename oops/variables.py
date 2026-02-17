#instance variable ex:-
class student:
    school = "holy mothers academy"
    def __init__(self, name, marks):
        self.name = name  #instance variable
        self.marks = marks #instance variable

    def show(self):
        schoolcity = "dhanbad"
        print(self.name, self.marks)
        print(schoolcity)
        print(self.school)
s1 = student("muskan" , 98)
s2 = student("vishnu",78)
s1.show()
s2.show()