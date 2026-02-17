#Print only name and email get method
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("-" * 30)



#GET request with query parameter userId=2
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 2})

if response.status_code == 200:
    posts = response.json()
    print("Number of posts:", len(posts))

#Verify status code 201 post request
import requests

data = {
    "title": "My New Post",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

if response.status_code == 201:
    print("Resource created successfully!")
else:
    print("Failed to create resourc")


#Raise exception if status code is not 200
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception("Request failed with status code:", response.status_code)

print("Request successful!")

#Print usernames in uppercase

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()

for user in users:
    print(user["username"].upper())

#Timeout handling

import requests
from requests.exceptions import Timeout

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )
    print("Request successful")
except Timeout:
    print("Request timed out!")


#Using Session object

import requests

session = requests.Session()

# First request
response1 = session.get("https://httpbin.org/cookies/set?mycookie=testvalue")

# Second request (cookie persists)
response2 = session.get("https://httpbin.org/cookies")

print("Cookies stored in session:")
print(response2.json())


#Upload a file using requests

import requests

response = requests.post("https://httpbin.org/post")

print("Server Response:")
print(response.json())

#Fetch posts
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    with open("posts.json", "w") as file:
        json.dump(response.json(), file, indent=4)

    print("Posts saved to posts.json")

