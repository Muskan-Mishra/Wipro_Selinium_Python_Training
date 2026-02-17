import requests
try:
    data ={
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }



    response = requests.put("https://api.restful-api.dev/objects/ff8081819c5368bb019c55a38560046a" , json = data)
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
