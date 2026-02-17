def make_pretty (func):
    def inner():
        print("i got decorated")
        func()
    return inner
@make_pretty
def vanillacake():
    print("i am the vanilla cake")
@make_pretty
def stawberrycake():
    print("i am the  stawberrycake")

vanillacake()
stawberrycake()

