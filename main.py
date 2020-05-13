import requests
import time
import datetime
import csv

from api import get_routes
from api import get_available_vehicles
from api import passenger_load_list
from api import get_current_datetime


agency_id = 643 # RIT Agency ID
route_name_list, route_id_list = get_routes(agency_id)

# print("Routes:",route_name)
# print("Route ID:",route_id)

# Get a list of passenger_load's for all buses(active and inactive)
# passenger_load_list = passenger_load_list(route_id_list,agency_id,route_name_list)


# today = get_current_datetime()
# print(today)

# Create first line of csv sheet
header = ['Day','Month','Year','Hour','Min','Sec']
header.extend(route_name_list)
print(header)


def create_row(agency_id):
    route_name_list, route_id_list = get_routes(agency_id)
    passenger_loads = passenger_load_list(route_id_list,agency_id,route_name_list)
    today = get_current_datetime()
    # print(today)

    # Create a single list with Current Date, Time and passenger_load
    today.extend(passenger_loads)
    row = today
    print(row)
    return row,today

# create_row(agency_id)

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    count = 0;
    while(1):
        count = count + 1
        print(count)
        rownow,today  = create_row(agency_id)
        writer.writerow(rownow)
        if(today[3]==18 & today[4]==10):
            break
            
