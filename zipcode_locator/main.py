from geopy.geocoders import Nominatim

#Create the geolocator object with a user agent
geolocator = Nominatim(user_agent="geoapiExercises")

place = input("Enter City Name: ").title()

#Geocode the location
location = geolocator.geocode(place)

#print the geolocation details
print(location)
