#1
def is_in_range(num, start, end):
    return start <= num <= end
print(is_in_range(5, 1, 10))

#2
def print_even_numbers():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)
print_even_numbers()
#3
def sum_1_to_100():
    return sum(range(1, 100))
print(sum_1_to_100())
#4
for i in range(1, 101):
    if i % 5== 0:
        print(i)
#5
numbers = list(range(50,101,5))
print(numbers)
#6
for i in range(1, 11):
    print(i, "square is", i*1)
#7
for i in range(-10, 11):
    print(i)

