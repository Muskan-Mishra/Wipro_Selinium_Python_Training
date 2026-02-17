fruits = ["orange" , "mango" , "cherry"]
for index,fruit in enumerate(fruits):
    print(index, fruit)

# enumerate with start value changed
for index,fruit in enumerate(fruits , start=1):
    print(index, fruit)

# enumerate with strings

word = "python"
for i, ch in enumerate(word):
    print(i, ch)

word = "python"
for i, ch in enumerate(word , start = 2):
    print(i, ch)

#enumerate with tuples
fruits = ("orange" , "mango" , "cherry")
for index,fruit in enumerate(fruits):
    print(index, fruit)

#real time scenario

test_cases = ["login" , "signup" , "checkout"]
for case_no, test in enumerate(test_cases, start =1):
    print(f"Executing Testcase {case_no}: {test}")

# accessing of the enumerate values
a = ['god' , 'is' , 'great']
b= enumerate(a)
nxt_val = next(b)
print(nxt_val)
print(nxt_val)


#duplicate detection using enumerate
#characters = ["krllin" , "goku" , " gohan", " piccolo" , "krllin" , "goku" , "vegeta" , "gohan" , "piccolo"  ]
#character_map = {character: [] for character in set(characters)}
#for index, character in enumerate


