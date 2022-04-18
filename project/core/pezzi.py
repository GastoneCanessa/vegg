pezzo di codice tolto da crea post view

geolocator= Nominatim(user_agent='measurements')
posts=Post.objects.all()#.order_by('-distance')
ip='95.237.149.43'
g = GeoIP2()
city = g.city(ip)
lat, lon =g.lat_lon(ip)
l_lat=lat
l_long=lon
pointA=(lat,lon)
b=[]
d=[]
distance=[]
for post in posts:
    city_=post.city
    destination=geolocator.geocode(city_)
    d_long=destination.longitude
    d_lat=destination.latitude
    pointB=(d_lat,d_long)
    distance_=round(geodesic(pointA,pointB).km ,2)
    distance.append(distance_)
    post.distance= distance_
    post.save()






    for post in posts:
        city_d=post.city
        destination=geolocator.geocode(city_d)
                # cordinate destinazione
        d_long=destination.longitude
        d_lat=destination.latitude
        pointB=(d_lat,d_long)
        distance_=round(geodesic(pointA,pointB).km ,2)
        #distance.append(distance_)
        distance[post.id] = distance_
        #post.distance = distance_
        #post.save()

    pairs = distance.items()
    filtered_dictionary = {key: value for key, value in pairs if value <= y}
    print(filtered_dictionary.keys())

    city_in_radius = Post.objects.filter(pk__in= filtered_dictionary.keys() ).values_list('city').distinct()
