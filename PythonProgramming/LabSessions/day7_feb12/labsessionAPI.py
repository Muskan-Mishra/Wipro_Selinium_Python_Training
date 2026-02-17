#get
import requests
try:
    response = requests.get("https://api.restful-api.dev/objects")
    print(response)

    if response.status_code == 200:
        print("status coede is 200 ok")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error:Received status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")




#post
import requests
try:
    data ={
  "category": "Platform",
  "name": "Mario",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85

    }
    response = requests.post("https://api.restful-api.dev/objects" , json = data)
    print(response)

    if response.status_code == 200:
        print("status coede is 200 ok")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error:Received status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")

