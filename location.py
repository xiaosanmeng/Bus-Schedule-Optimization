# Get Vehicle Location

# Province Route ID: 4013312
# Evening Campus Route ID: 4013322


import requests

url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

# Province Route ID: 4013312 ; RIT Agency ID: 643
querystring = {"routes":"4013322","callback":"call","agencies":"643"} # Evening Campus Shuttle
# querystring = {"routes":"4013312","callback":"call","agencies":"643"}   # Province

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
# Get the vehicle Location
location = (json['data']['643'][0]['location'])
print("Location: " + str(location))

lat = location['lat']   # Get vehicle Latitude
print("Latitude: " + str(lat))

lon = location['lng']   # Get vehicle Longitude
print("Longitude: " + str(lon))
