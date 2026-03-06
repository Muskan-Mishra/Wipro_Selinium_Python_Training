class Student:

    studentname = "ravi"
    studentID = 567

    #create fun to access the data
    def displaystudentdetails(self):
        print(self.studentname)
        print(self.studentID)

#create the object of the class
a = Student()
a.displaystudentdetails()

