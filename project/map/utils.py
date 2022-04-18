from django.contrib.gis.geoip2 import GeoIP2
from geopy.geocoders import  Nominatim
from geopy.distance import geodesic

def get_ip_address(request):
    x_forwarded_for= request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip=x_forwarded_for.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip

# heler function
def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon =g.lat_lon(ip)
    return country,city,lat,lon

def get_center_cordinates(latA,longA,latB=None,longB=None):
    cord=(latA,longA)
    if latB:
        cord=[(latA+latB)/2,(longA+longB)/2]
    return cord

def get_zoom(distance):
    if  distance <= 100:
        return 8
    elif distance  >100 and distance<=5000:
        return  4
    else :
        return 2

def get_posts_in_radius(radius, posts, pointA,):
    geolocator= Nominatim(user_agent='measurements')
    distance = {}
    for post in posts:
        city_d=post.city
        destination=geolocator.geocode(city_d)
        d_long=destination.longitude
        d_lat=destination.latitude
        pointB=(d_lat,d_long)
        distance_=round(geodesic(pointA,pointB).km ,2)
        distance[post.id] = distance_
    pairs = distance.items()
    filtered_dictionary = {key: value for key, value in pairs if value <= radius}
    return filtered_dictionary

def distance(posts, pointA):
    geolocator= Nominatim(user_agent='measurements')
    distance = {}
    for post in posts:
        city_d=post.city
        destination=geolocator.geocode(city_d)
        d_long=destination.longitude
        d_lat=destination.latitude
        pointB=(d_lat,d_long)
        distance_=round(geodesic(pointA,pointB).km ,2)
        distance[post.id] = distance_
    return distance

def from_ip_to_cordinate(ip):
    g = GeoIP2()
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    pointA= (lat,lon)
    return pointA

def from_ip_to_city(ip):
    g = GeoIP2()
    city = g.city(ip)
    return city
