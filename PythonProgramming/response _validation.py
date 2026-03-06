import requests
from certifi import contents

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
        print(response.text)
        print(response.content)
        print(response.status_code)
        print(response.headers)
        print(response.history)
        print(response.url)
        content_type = response.headers.get('Content_type')
        print(content_type)
    else:
        print(f"Error:Received status code{response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
