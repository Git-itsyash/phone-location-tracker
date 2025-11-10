import phonenumbers
import opencage
import folium
from phonenumbers import geocoder,timezone
number = str(input("enter your number with counter code:")) 
pepnumber = phonenumbers.parse(number)
time=timezone.time_zones_for_number(pepnumber)
location = geocoder.description_for_number(pepnumber, "en")
print(location)
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
# enter your api key 
key = 'YOUR API KEY'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
