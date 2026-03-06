# custom iterator that prints numbers from 1 to 5

class OneToFive:
    def __init__(self):
        self.x = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.x <= 5:
            val = self.x
            self.x += 1
            return val
        raise StopIteration

print("1 to 5 iterator")
for i in OneToFive():
    print(i)

class EvenIterator:
    def __init__(self):
        self.x = 2
    def __iter__(self):
        return self
    def __next__(self):
        val = self.x
        self.x += 2
        return val

print("\nNext even numbers")
e = EvenIterator()
for _ in range(5):
    print(next(e))