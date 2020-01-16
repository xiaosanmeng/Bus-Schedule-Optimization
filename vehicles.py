# Get Vehicle Data

# Province Route ID: 4013312

import requests

url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

# Province Route ID: 4013312 ; RIT Agency ID: 643
querystring = {"routes":"4013312","callback":"call","agencies":"643"}

headers = {
    'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
    'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
    }


response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
# print(response.headers)
json = response.json()
print(json)

# RIT Agency ID: 643
# Get the passenger_load for the Bus
passenger_load = (json['data']['643'][0]['passenger_load'])
passenger_load = round(passenger_load,2) * 100  # Convert to Percentage
print("Pasenger Load: " + str(passenger_load) + "%")
