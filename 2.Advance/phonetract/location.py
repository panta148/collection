import geocoder
import folium
g = geocoder.ip('me')
myadd = g.latlng
# this will print your latitude and the longitude location
print(myadd)
