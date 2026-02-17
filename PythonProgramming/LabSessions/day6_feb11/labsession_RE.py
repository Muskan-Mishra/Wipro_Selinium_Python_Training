import re


# 1. Check if a string contains only digits
def contains_only_digits(text):
    pattern = r'^\d+$'
    return bool(re.match(pattern, text))


# 2. Match a 10-digit mobile number
def match_mobile_number(text):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, text))


# 3. Find all lowercase letters in a string
def find_lowercase_letters(text):
    pattern = r'[a-z]'
    return re.findall(pattern, text)


# 4. Extract all uppercase letters from a sentence
def find_uppercase_letters(text):
    pattern = r'[A-Z]'
    return re.findall(pattern, text)


# 5. Match a string that starts with "Hello"
def starts_with_hello(text):
    pattern = r'^Hello'
    return bool(re.search(pattern, text))


# 6. Match a string that ends with "world"
def ends_with_world(text):
    pattern = r'world$'
    return bool(re.search(pattern, text))


# 7. Find all words separated by spaces
def find_all_words(text):
    pattern = r'\b\w+\b'
    return re.findall(pattern, text)


# 8. Match exactly 5 characters
def match_exactly_5_chars(text):
    pattern = r'^.{5}$'
    return bool(re.match(pattern, text))


# 9. Find all occurrences of the word "python" (case-insensitive)
def find_python_occurrences(text):
    pattern = r'\bpython\b'
    return re.findall(pattern, text, re.IGNORECASE)


# Test examples
if __name__ == "__main__":
    # Test each function
    print("1. Contains only digits '12345':", contains_only_digits("12345"))
    print("1. Contains only digits '123a5':", contains_only_digits("123a5"))

    print("\n2. Match mobile '9876543210':", match_mobile_number("9876543210"))
    print("2. Match mobile '98765':", match_mobile_number("98765"))

    print("\n3. Lowercase letters in 'Hello World':", find_lowercase_letters("Hello World"))

    print("\n4. Uppercase letters in 'Hello World':", find_uppercase_letters("Hello World"))

    print("\n5. Starts with 'Hello' 'Hello there':", starts_with_hello("Hello there"))
    print("5. Starts with 'Hello' 'Hi Hello':", starts_with_hello("Hi Hello"))

    print("\n6. Ends with 'world' 'Hello world':", ends_with_world("Hello world"))
    print("6. Ends with 'world' 'world hello':", ends_with_world("world hello"))

    print("\n7. All words in 'This is a test':", find_all_words("This is a test"))

    print("\n8. Exactly 5 chars 'abcde':", match_exactly_5_chars("abcde"))
    print("8. Exactly 5 chars 'abcd':", match_exactly_5_chars("abcd"))

    print("\n9. Python occurrences 'Python is python and PYTHON':",
          find_python_occurrences("Python is python and PYTHON"))
import re

text = "Hello python World HELLO world 1234567890 python PYTHON hello world"

print("1. Write a regex to check if a string contains only digits.")
print(bool(re.fullmatch(r"\d+", "123456")))

print("2. Write a pattern to match a 10-digit mobile number.")
print(re.findall(r"\b\d{10}\b", text))

print("3. Find all lowercase letters in a string.")
print(re.findall(r"[a-z]", text))

print("4. Extract all uppercase letters from a sentence.")
print(re.findall(r"[A-Z]", text))

print("5. Match a string that starts with 'Hello'.")
print(bool(re.match(r"^Hello", text)))

print("6. Match a string that ends with 'world'.")
print(bool(re.search(r"world$", text)))

print("7. Find all words separated by spaces.")
print(re.findall(r"\S+", text))

print("8. Match exactly 5 characters.")
print(re.findall(r"\b\w{5}\b", text))

print("9. Find all occurrences of the word 'python' (case-sensitive).")
print(re.findall(r"\bpython\b", text,re.IGNORECASE))

print("10. Replace all spaces in a string with underscores.")
print(re.sub(r"\s", "_", text))