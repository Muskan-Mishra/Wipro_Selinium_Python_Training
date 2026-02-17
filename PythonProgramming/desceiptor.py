class desc:
    def __get__(self, instance, owner):
        print("getting the value")
        return 10


class test:
    x =  desc()

t = test()
print(t.x)


class mydesc:
    def __get__(self, instance, owner):
        return  instance._value
    def __set__(self, instance, value):
        print("setting the value")
        instance._value = value

class test:
    x = mydesc()
t = test()
t.x = 100
print(t.x)

class name:
    def __get__(self, instance, owner):
        return  instance._value
    def __set__(self, instance, value):
        instance._value = value

    def __delete__(self, instance):
        print("deleting name")
        del instance._value

class person:
    name = name()
p = person()
p.name = "muskan"
del  p.name





