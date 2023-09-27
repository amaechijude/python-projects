from geopy.geocoders import Nominatim
import time
from pprint import pprint

#Create the geolocator object with a user agent
app = Nominatim(user_agent="tutorial")

#place = input("Enter City Name: ").title()

#Geocode the location
location = app.geocode("Nairobi, Kenya").raw

#print the geolocation details
pprint(location)
