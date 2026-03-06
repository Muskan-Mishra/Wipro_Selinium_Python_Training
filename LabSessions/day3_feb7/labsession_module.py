import  random
import string
char = random.choice(string.ascii_letters)
print(char)
length = random.randint(5,10)
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
print("random string:" , random_string)

fixed_length = 6
fixed_string = ''.join(random.choice(string.ascii_letters) for _ in range(fixed_length))
print(fixed_string)