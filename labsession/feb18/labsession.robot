
*** Settings ***
Library    Collections

*** Variables ***
${NAME}        Priyadarshee
${CITY}        Patna
@{FRUITS}      Apple    Banana    Mango
&{USER}        name=Priyadarshee    role=Tester    age=22

*** Test Cases ***

# Create a scalar variable ${NAME} and print it
Print Scalar Variable
    Log    Name is: ${NAME}

# Assign two numbers to variables and print their sum
Add Two Numbers
    ${a}=    Set Variable    10
    ${b}=    Set Variable    20
    ${sum}=  Evaluate    ${a} + ${b}
    Log    Sum is: ${sum}

# Create a variable ${CITY} and use it inside a sentence
Use Variable In Sentence
    Log    I live in ${CITY} city.

# Reassign a variable value inside a test case and log the updated value
Reassign Variable
    ${NAME}=    Set Variable    Kumar
    Log    Updated Name is: ${NAME}

# Create a list variable @{FRUITS} and print the first item
Print First Fruit
    Log    First fruit is: ${FRUITS}[0]

# Loop through a list variable and print each element
Loop Through List
    FOR    ${fruit}    IN    @{FRUITS}
        Log    Fruit: ${fruit}
    END

#  Find the length of a list variable
Find List Length
    ${length}=    Get Length    ${FRUITS}
    Log    Total fruits: ${length}

# Create a dictionary variable &{USER} and print one key value
Print Dictionary Value
    Log    User Name: ${USER}[name]

# Add a new key-value pair to a dictionary variable
Add Key To Dictionary
    Set To Dictionary    ${USER}    city=Patna
    Log    Updated Dictionary: ${USER}

# Access dictionary values inside a loop and print key and value
Loop Through Dictionary
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} = ${value}
    END