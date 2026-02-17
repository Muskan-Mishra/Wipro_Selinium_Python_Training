#when bd connection has to be closed
class desct:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("closing the connection")

a = desct
print("end the program")
del a


class filehandler:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print("file is opened")

    def readfile(self, filename):
        print("reading the file")

    def __del__(self):
        self.file.close()
        print("file closed")

f = filehandler("test.txt")
f.readfile("test.txt")
del f

