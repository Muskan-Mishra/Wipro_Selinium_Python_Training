#1
import json


try:
    with open(
            "/dataformats//name.json",
        'r') as file:
        data = json.load(file)
        print(data)
        file.close
except FileNotFoundError:
    print("error: file not found. please check the file name.")

#2
try:
    num = int(input("enter an integer"))
    print(num)
except ValueError:
    print("invalid input ! plaese enetr a valid integer.")

#3