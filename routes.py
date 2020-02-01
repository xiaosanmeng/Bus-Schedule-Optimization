import requests

url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"

# RIT Agency ID: 643
querystring = {"callback":"call","agencies":"643"}

headers = {
    'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
    'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)

json = response.json()
# print(json)

routes = json['data']['643']    # Get the different routes for RIT(643)
print("Number of Routes: " + str(len(routes)))


# Get the data for each route
route_name = []
route_id = []
for route in routes:
    route_name.append(route['long_name'])
    route_id.append(route['route_id'])
# print(route_name,route_id)

# Print route_id for each route
for route in range(len(routes)):
    print(route_name[route] + ": " + route_id[route])

# from api import get_vehicles
# get_vehicles(643,route_id[0])
