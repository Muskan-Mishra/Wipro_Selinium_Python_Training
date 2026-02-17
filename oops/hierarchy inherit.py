class employee:
    def login(self):
        print("employee is logged in")

class developer(employee):
    def write_code(self):
        print("writing code")

class tester(employee):
    def test_app(self):
        print("test the application")

dev = developer()
test = tester()

dev.login()
dev.write_code()
test.login()
test.test_app()
