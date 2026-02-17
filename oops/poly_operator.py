class number:
    def __init__(self , value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
    def __sub__(self, other):
        return self.value - other.value
    def __mul__(self, other):
        return self.value * other.value
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value


onj1 = number(8)
obj2 = number(6)
print(onj1+obj2)
print(onj1-obj2)
print(onj1*obj2)
print(onj1==obj2)
print(onj1<obj2)
print(onj1>obj2)
