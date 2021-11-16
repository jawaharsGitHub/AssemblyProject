import phonenumbers
import opencage
import folium
import codecs
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

phoneNumber = '+919443612036';


print(phoneNumber)

pepNo = phonenumbers.parse(phoneNumber, "CH")
location = geocoder.description_for_number(pepNo, "en")
c = phonenumbers.parse(phoneNumber, "RO")
service_provider = carrier.name_for_number(c, "en")
print(location, service_provider)

key = 'e4fd95843a164f0b90c0e404022c402d'

geocoder = OpenCageGeocode(key)
results = geocoder.geocode(str(location))
print(results)

#lat = 9.348093
#lng = 78.6811106


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)


my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)
my_map.save('mymap.html')
codecs.open('mymap.html')





