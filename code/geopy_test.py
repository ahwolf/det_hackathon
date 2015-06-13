from geopy.geocoders import Nominatim
from geopy.distance import vincenty


newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)

print(vincenty(newport_ri, cleveland_oh).miles)

# geolocator = Nominatim()

# location = geolocator.geocode("175 5th Avenue NYC")
# print(location.address)
# print((location.latitude, location.longitude))
