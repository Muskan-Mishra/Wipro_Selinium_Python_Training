# 1. Filter even numbers
# 2. Square them
# 3. Find t
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8]

#Filter even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))

#Square them
squared = list(map(lambda x: x * x, nums))

#Find sum using reduce
total_sum = reduce(lambda x, y: x + y, nums)

print("Even Numbers:", even_nums)
print("Squared Even Numbers:", squared)
print("Sum of Squares:", total_sum)






# From a list of salaries:
# 1. Filter salaries > 30000
# 2. Add 10% hike
# 3. Find total payout

salaries = [25000, 40000, 32000, 18000]

#Filter salaries greater than 30000
high_salary = list(filter(lambda x: x > 30000, salaries))

#Add 10% hike
hiked_salary = list(map(lambda x: x + x * 0.10, high_salary))

#Find total payout
total_payout = reduce(lambda x, y: x + y, hiked_salary)

print("\nFiltered Salaries:", high_salary)
print("After 10% Hike:", hiked_salary)
print("Total Payout:", total_payout)

# Python program to sort a list of tuples using lambda

# Sort by the second element of each tuple.

# List of tuples
data = [(1, 3), (4, 1), (2, 2), (5, 0)]

# Sorting using lambda
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

#2. Python program to extract year, month, date, and time using lambda

from datetime import datetime

# Current date and time
now = datetime.now()

# Lambda functions
get_year = lambda x: x.year
get_month = lambda x: x.month
get_date = lambda x: x.day
get_time = lambda x: x.time()

print("Year:", get_year(now))
print("Month:", get_month(now))
print("Date:", get_date(now))
print("Time:", get_time(now))
