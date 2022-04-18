from django.shortcuts import render, get_object_or_404
from .forms import  ResearchFormMap
from core.models import  Post
from .utils import get_posts_in_radius, from_ip_to_cordinate, from_ip_to_city

from geopy.geocoders import  Nominatim
import folium
from folium import plugins

def homepage(request):
    ip='95.237.149.43'
    city = from_ip_to_city(ip)
    pointA = from_ip_to_cordinate(ip)
    form= ResearchFormMap(request.POST or None)
    geolocator= Nominatim(user_agent='measurements')
    x= 20000
    y= 20
    if form.is_valid():
        if form.cleaned_data.get('position')==True:
            y=form.cleaned_data.get('search_radius')
            x=y*1000
            pointA=pointA
        else:
            city_o_=form.cleaned_data.get('city')
            y=form.cleaned_data.get('search_radius')
            x=y*1000
            city_o=geolocator.geocode(city_o_)
            o_long=city_o.longitude
            o_lat=city_o.latitude
            print(o_long)
            print(o_lat)
            pointA=(o_lat,o_long)

    posts=Post.objects.all()
    filtered_dictionary = get_posts_in_radius(y,posts,pointA)
    city_in_radius = Post.objects.filter(pk__in= filtered_dictionary.keys() ).values_list('city').distinct()

    map = folium.Map(width=800, height=500, location=pointA)
    folium.Marker(
    pointA,tooltip="click here for more",popup=city['city'],
    icon=folium.Icon(color="purple")).add_to(map)
    feature_group = folium.FeatureGroup("Locations")

    for city_ in city_in_radius:
        city_=city_[0]
        destination = geolocator.geocode(city_)
        d_long = destination.longitude
        d_lat = destination.latitude
        users_for_city = Post.objects.filter(city=city_).values_list('author_post').distinct()

        for user_ in users_for_city:
            user = user_
            popup = folium.Popup('<a href=[users/] "target="_blank"> [text for link goes here] </a>')
            feature_group.add_child(folium.Marker([d_lat,d_long],tooltip = "click here for more",popup=f"<a href=user/{user}  target='_blank'>{user} da {city_}</a>" ,
            icon = folium.Icon(color = "purple")))
    #feature_group.add_child(folium.PolyLine(locations=[pointA, co],weight=2,color='blue'))
    feature_group.add_child(folium.Circle(
    location = pointA,
    popup = "reserch radius",
    color = "#bbadff",
    radius = x,
    fill = True,
    opacity = 0.8,
    fill_opacity = 0.05,
    ))
    map.add_child(feature_group)
    map = map._repr_html_()
    context = {'map':map,'form':form}
    return render(request, 'map/map.html', context)
