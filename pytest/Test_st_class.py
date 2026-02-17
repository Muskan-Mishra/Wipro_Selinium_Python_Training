class Testclass:
    def setup_class(cls):
        print("API Authorization needed with username and password")

    def teardown_class(cls):
        print("API Authorization close")

    def setup_method(method):
        print("opening the browser")

    def teardown_method(method):
        print("closing the browser")

    def testcase1(self):
        print("Testcase1 is exceuted")

    def testcase2(self):
        print("Testcase2 is exceuted")

    def testcase3(self):
        print("Testcase3 is exceuted")

class Testclass2:
    def testcase1(self):
        print("Testcase1 is exceuted")

    def testcase2(self):
        print("Testcase2 is exceuted")

    def testcase3(self):
        print("Testcase3 is exceuted")

