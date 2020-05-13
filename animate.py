# Plot vehicle data based on Sparkfun's matplotlib real-time update tutorial.

# Province Route ID: 4013312
# Evening Campus Route ID: 4013322

# Libraries required to plot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Libraries for map stuff
import numpy as np
import pandas as pd


# Libraries required for getting data
import requests


url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

# Province Route ID: 4013312 ; RIT Agency ID: 643
querystring = {"routes":"4013322","callback":"call","agencies":"643"} # Evening Campus Shuttle
# querystring = {"routes":"4013312","callback":"call","agencies":"643"}   # Province

headers = {
    'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
    'x-rapidapi-key': "c7a9a279b1msh49ce82192ac5ef8p1830cejsnf6c553ccadea"
    }


def get_location():
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

    return lat,lon

lat, lon = get_location()

map = plt.imread('C:/Users/Jonathan/Documents/GitHub/Transloc-Bus-Tracking/map.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(lon, lat, zorder=1, alpha= 0.2, c='b', s=10)
BBox = [-77.6895, -77.6517, 43.0925, 43.0748]
ax.imshow(map, zorder=0, extent = BBox, aspect= 'equal')
