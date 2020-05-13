![Banner](https://github.com/jonathanrjpereira/Bus-Schedule-Optimization/blob/master/img/banner.png)

The projects aims to optimize bus schedules in order lower costs and reduce carbon emissions using passenger occupancy data collected via the Transloc API.

# Working
## Data Collection
The passenger occupancy data for a particular bus route is sampled periodically via the Transloc API and stored in a database.  More information about the data collection can be found in the later part of this tutorial.

## Sample Data
The data of several buses and buses routes can be sampled and stored in a database. In our example we will focus on one particular data sample for a single bus that plys a single bus route. The data snippet is for the Weekend RIT Inn bus and was sampled in March for approximately 5 hours (6 PM to 10:40 PM) in the evening (The data collection was limited due to the Coronavirus pandemic). The bus route consists of 6 separate stops and a round trip takes 35 minutes to complete. The bus schedule begins at 7:00 AM and ends at 1:40 AM. The full bus schedule can be found here.

## Data Processing
The data is sampled just below the APIs rate limit (~2.2/min) and stored in a CSV file. First, the data is averaged for each minute (1 minute bins). This ensures each minute of the total sampling time period (approx. 5 hours) contains a single passenger occupancy value associated with it. The data is also averaged for 5 minute bins. Since the round trip time is 35 minutes, the data is also averaged for 35 minute bins. The 35 minute bins will be the basis upon which the schedule will be optimized. The figure below shows the average passenger occupancy (%) for the 1 minute, 5 minute and 35 minute bins. 
![Weekend RIT Inn Occupancy Average Bins](https://github.com/jonathanrjpereira/Transloc-Bus-Tracking/blob/master/img/Weekend%20RIT%20Inn.svg)

In the above figure, we can observe, the average passenger occupancy for each of the eight 35 minute round trips. The highest average passenger occupancy occurs for the 1st round trip which started at 18:05 PM. 

## Passenger Occupancy Thresholding
The project focuses on creating optimized bus schedules based on past passenger occupancy data. 
 
In order to optimize the bus schedule we can set a threshold value for whether a bus should operate for a particular round trip timeslot. To begin with we can assume a threshold of 10% passenger occupancy i.e. a bus will operate for a particular round trip timeslot only if the average passenger occupancy for that timeslot is greater than equal to 10% of the buses total capacity. The first row in the figure below shows the 35 minute time slots for a 10% threshold. The yellow block indicates that the average passenger occupancy for that time slot was greater than or equal to 10% while the remaining blue blocks did not meet the threshold value.

## Dynamic Thresholding
If we were to use a single threshold value, for example 10%, a condition may arise when no bus is scheduled for a long period of time since passenger occupancy is extremely low during non-peak hours especially in the evening once most classes are over. This can be observed by several adjacent blue colored time slots in the first row of the figure below.

![Optimized Bus Schedule](https://github.com/jonathanrjpereira/Transloc-Bus-Tracking/blob/master/img/Optimized.svg)

By creating separate thresholds for typical working/class hours (9AM to 7PM) and non-working hours (7PM onwards), we can further optimize the bus schedule whilst ensuring a convenient service for passengers. For example,  if a threshold of 5% is used for all time slots beginning around 7 PM, we can see an increase in the number of yellow blocks indicating that the bus will operate for that particular time slot as depicted by the second row in the above figure. 

## Schedule Optimization
The last row in the figure below shows how the bus schedule can be optimized by implementing dynamic thresholding i.e. 10% during working hours and 5% during non-working hours. The green blocks indicate time slots for which a bus will operate while the red blocks indicate that a bus will not run during that particular timeslot. For this 5 hour data snippet the schedule was optimized such that bus operates for only 4/8 time slots or 50% of the total operation window. Even at this rate, the bus will not meet its full capacity i.e. overcrowding will not take place. 

![Combined Heatmaps](https://github.com/jonathanrjpereira/Transloc-Bus-Tracking/blob/master/img/Combined.svg)

# Results
From the above figure, we can observe that the bus will run for half the time it typically does as a result of the dynamic thresholding optimization algorithm. The round trip Weekend RIT Inn bus route is approximately 10 miles. Hence for the 5 hour time slot, the distance covered by the bus will decrease by 40 miles. 

According to the US Department of Energy, the average fuel economy for a transit bus is 3.26 miles per gallon of gasoline[\[1\]](https://afdc.energy.gov/data/10310). The round trip Weekend RIT Inn bus route is approximately 10 miles. Hence a single round trip should consume around 3 gallons of fuel. For this 5 hour data snippet itself, the optimized schedule will save around 12 gallons of fuel per day, 24 gallons per Weekend, and around 960 gallons per year (assuming 40 working weeks). 

At $1.5 per gallon of fuel, the total fuel cost can be reduced by approximately $1,440 per year (for just a single bus based on 5 hours of data). 

According to the US Department of Transportation, bus transit emits 0.64 lbs of CO2 per passenger mile[\[2\]](https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/PublicTransportationsRoleInRespondingToClimateChange2010.pdf). Hence for 40 miles x 2 days x 40 weeks x 0.64, a single bus (5 hour time slot) can reduce its CO2 emissions by more than 2000lbs. 

**Note**: Passenger miles = vehicle miles x average number of passengers on vehicle. Normalizing by passenger miles allows for comparison between vehicles carrying different numbers of passengers

# Code
##  Prerequisites
You can install the necessary dependencies by running the requirements.txt file.
 - Python 3x
 - Numpy
 - Pandas
 - Matplotlib
 - Seaborn
 - Requests

## Transloc API
The Transloc API provides API calls that can be used to retrieve a list of Agencies. Using an Agency ID, we can get a list of routes for a particular agency. We can also get location, arrival time, compass and passenger occupancy data for buses operating on a particular route. More information can be found on the Transloc API website.

We use the Requests library to make API requests and retrieve the passenger occupancy data. The code factors in the API request rate limit and ensure that it does not exceed the limit.

## Storing the Data
The sampled passenger occupancy data for each bus is stored in a new line within a CSV file alongwith the current timestamp using the CSV library.

## Data Visulization
A Pandas dataframe is created for each bus route (CSV columns) and the heatmaps and thresolding graphs were created using the Seaborn and Matplotlib heatmap functionality.   


# References

1. [US Department of Energy - Average Fuel Economy by Vehicle Category](https://afdc.energy.gov/data/10310)
2. [US Department of Transportation - Pound of CO2 per Passenger Mile - Public Transportation's Role in Reducing Greenhouse Gas Emissions](https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/PublicTransportationsRoleInRespondingToClimateChange2010.pdf)


# Contributing

Are you a programmer, engineer or hobbyist who has a great idea for a new feature in this project? Maybe you have a good idea for a bug fix? Feel free to grab our code & schematics from Github and tinker with it. Don't forget to smash those ⭐️ & Pull Request buttons. [Contributor List](https://github.com/jonathanrjpereira/Transloc-Bus-Tracking/graphs/contributors)

Made with ❤️ by [Jonathan Pereira](https://github.com/jonathanrjpereira)
