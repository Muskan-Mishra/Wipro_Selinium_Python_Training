#1
def numbers(n):
    for i in range(1, n+1):
        yield i
for i in  numbers(10):
    print(i)

#2
def evenno(n):
    for i in range(2, n+1 , 2):
        yield i
for i in evenno(20):
    print(i)

#3
def read_file(filename):
    with open(
        "C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//employee.json",
        'r') as file:
        for line in file:
            yield line. strip()
for line in read_file("sample.txt"):
    print(line)
#4
def fibonacci(n):
    a , b = 0 , 1
    for _ in range(n):
        yield a
        a , b = b , a + b
for i in fibonacci(14):
    print(i)

#5
def retry_attempts(max_tries=3):
    attempt = 1
    while attempt <= max_tries:
        yield f"retry attempt {attempt}"
        attempt += 1

for attempt in retry_attempts():
    print(attempt)
