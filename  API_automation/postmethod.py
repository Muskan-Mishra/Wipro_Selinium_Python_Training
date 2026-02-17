import requests
try:
    data ={
  "category": "Platform",
  "name": "Mario",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85

    }
    response = requests.post("https://videogamedb.uk:443/api/v2/videogame" , json = data)
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




