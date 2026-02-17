import requests
try:
    
    response = requests.delete("https://videogamedb.uk:443/api/v2/videogame/1")
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
