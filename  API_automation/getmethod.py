import requests
from requests.auth import HTTPBasicAuth

try:
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame")
    print(response)

    if response.status_code == 200:
        print("status coede is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error:Received status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")



import requests
try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"


    }
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame", auth=HTTPBasicAuth('username', 'password'),timeout=5, headers=headers)
    print(response)

    if response.status_code == 200:
        print("status coede is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error:Received status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
