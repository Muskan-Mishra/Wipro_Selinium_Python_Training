#square of a no
from PythonProgramming.list import even_numbers

sqs = [x**2 for x in range (1,6)]
print(sqs)

#with the condition
evennumbers = [x for x in range(10) if x %2==0]
print(evennumbers)

#dic comphresion increase by 10%
salary = {"a":5000, "b":6000, "c":7000}
updated_sal = {k: v + 0.1 * v for k, v in salary.items()}
print(updated_sal)

#filtering of dic
employees ={
    "muskan": "active",
    "uma":"inactive",
     "pooja": "active"
}
active_employees = {k: v for k, v in employees.items() if v == 'active'}
print(active_employees)

# set comphresions

sqs = { x**2 for x in range (1,6)}
print(sqs)

# with the condition
evennumbers = [x for x in range(10) if x %2==0]
print(evennumbers)



