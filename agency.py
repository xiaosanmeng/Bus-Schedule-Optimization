# Get the list of Agency IDs for Transloc
# RIT agency_id: 643

# py -2 agency.py
import requests
import re
# import time
# import argparse

url = "https://transloc-api-1-2.p.rapidapi.com/agencies.json"

querystring = {"callback":"call"}

headers = {
    'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
    'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# {"long_name": "Rochester Institute of Technology", "language": "en", "position":
# {"lat": 43.1591350688, "lng": -77.6153564453}, "name": "rit", "short_name": "RIT",
# "phone": null, "url": "http://www.rit.edu/#272", "timezone": "US/Eastern",
# "bounding_box": [{"lat": 43.050302573532576, "lng": -77.68312454223008},
# {"lat": 43.105359468098676, "lng": -77.62861251827928}],
# "agency_id": "643"},
