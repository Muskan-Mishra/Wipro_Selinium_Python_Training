#1
def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

# Example
nums = [1, 2, 3, 4, 5]
print("Sum:", sum_list(nums))

#2
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example
print("Maximum:", max_of_three(10, 25, 15))