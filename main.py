import requests
import time
import datetime


from api import get_routes
from api import get_available_vehicles
from api import passenger_load_list


agency_id = 643 # RIT Agency ID
route_name_list, route_id_list = get_routes(agency_id)

# print("Routes:",route_name)
# print("Route ID:",route_id)

# Get a list of passenger_load's for all buses(active and inactive)
passenger_load_list(route_id_list,agency_id,route_name_list)

print(get_datetime())
