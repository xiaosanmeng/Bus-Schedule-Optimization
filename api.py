import requests
import time
import datetime




# ---------------------------------#
def get_routes(agency_id):
    url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"

    # RIT Agency ID: 643
    querystring = {"callback":"call","agencies":agency_id}

    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)

    json = response.json()
    # print(json)

    routes = json['data']['643']    # Get the different routes for RIT(643)
    # print("Number of Routes: " + str(len(routes)))


    # Get the data for each route
    route_name = []
    route_id = []
    for route in routes:
        route_name.append(route['long_name'])
        route_id.append(route['route_id'])
    # print(route_name,route_id)

    # Print route_id for each route
    # for route in range(len(routes)):
    #     # print(route_name[route] + ": " + route_id[route])
    return route_name, route_id


# -----------------------------------------------------------------------------#
def get_vehicles(route_id,agency_id):
    url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

    # Province Route ID: 4013312 ; RIT Agency ID: 643
    # querystring = {"routes":"4013312","callback":"call","agencies":"643"}
    querystring = {"routes":route_id,"callback":"call","agencies":agency_id}

    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
        }


    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    # print(response.headers)
    json = response.json()
    # print(json)

    # RIT Agency ID: 643
    # Get the passenger_load for the Bus
    passenger_load = (json['data']['643'][0]['passenger_load'])
    passenger_load = round(passenger_load,2) * 100  # Convert to Percentage
    print("Pasenger Load: " + str(passenger_load) + "%")



# -----------------------------------------------------------------------------#
def get_available_vehicles(route_id,agency_id,route_name):
    url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

    # Province Route ID: 4013312 ; RIT Agency ID: 643
    # querystring = {"routes":"4013312","callback":"call","agencies":"643"}
    querystring = {"routes":route_id,"callback":"call","agencies":agency_id}

    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
        }


    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    # print(response.headers)
    json = response.json()
    # print(json)

    # Get rate limit
    rate_limit = (json['rate_limit'])
    # print("Rate Limit: " + str(rate_limit))

    # Check if the route is active or not. i.e. if data for the route is available.
    route_status = len((json['data']))
    if route_status>0:
        # RIT Agency ID: 643
        # Get the passenger_load for the Bus
        # passenger_load = (json['data']['643'][0]['passenger_load'])
        # passenger_load = round(passenger_load,2) * 100  # Convert to Percentage
        # print(str(route_name) + "Pasenger Load: " + str(passenger_load) + "%")

        passenger_load = (json['data']['643'][0]['passenger_load'])
        passenger_load = round(passenger_load,3) * 100  # Convert to Percentage
        # print(str(route_name) + "Pasenger Load: " + str(passenger_load) + "%")
        return passenger_load, rate_limit
    else:
        passenger_load = 0  # Route Inactive. Hence set passenger_load to 0.
        return passenger_load, rate_limit



# -----------------------------------------------------------------------------#
# Make a list of passenger_load for both active and inactive route/vehicles
def passenger_load_list(route_id_list,agency_id,route_name_list):
    passenger_load_list = []
    for route_id in route_id_list:
        route_name = route_name_list[route_id_list.index(route_id)]
        passenger_load, rate_limit = get_available_vehicles(route_id,agency_id,route_name)
        if passenger_load == None:
            passenger_load_list.append(0)
        else:
            passenger_load_list.append(passenger_load)
        time.sleep(rate_limit*1.1)  # Limit API requests to the rate_limit times 1.1

    # print("passenger_load_list",passenger_load_list)
    return passenger_load_list

# -----------------------------------------------------------------------------#
# Return the current date and time
def get_current_datetime():
    dt = datetime.datetime.today()
    day = dt.day
    mon = dt.month
    yr = dt.year
    hr = dt.hour
    min = dt.minute
    sec = dt.second
    today_datetime = [day, mon, yr, hr, min, sec]
    # today_datetime.extend((day, mon, yr, hr, min, sec))
    return today_datetime
