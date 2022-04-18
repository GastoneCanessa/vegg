import operator
from users.models import CustomUser
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm, SpecificheRicercaForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import  DeleteView

from geopy.geocoders import  Nominatim
from geopy.distance import geodesic
import folium
from django.contrib.gis.geoip2 import GeoIP2
from folium import plugins

from map.utils import get_posts_in_radius, from_ip_to_cordinate, from_ip_to_city, distance
from django.db.models import Case, When

def posts_view(request):
    ip='95.237.149.43'
    city = from_ip_to_city(ip)
    pointA = from_ip_to_cordinate(ip)
    x= 20000
    y= 30
    posts=Post.objects.all()
    distancee = distance(posts, pointA)
    distanceee = dict(sorted(distancee.items(), key=operator.itemgetter(1)))
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(distanceee.keys())])
    posts = Post.objects.filter(pk__in= distanceee.keys()).order_by(preserved)
    context={"posts":posts,'distance':distancee}
    return render(request,"core/home.html",context)

@login_required
def create_post_view(request):
    if request.method == "POST":
        form=PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.user)
            form.instance.author_post = request.user
            form.instance.city = request.user.city
            new_post=form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form=PostModelForm()
    context={"form":form}
    return render(request,"core/post_form.html",context)

def user_profile_view(request, username):
    user= get_object_or_404(CustomUser.objects.all(),username=username)
    user_=CustomUser.objects.filter(username=username)
    user_posts = Post.objects.filter(author_post=user).order_by("-pk")
    context={'user': user ,'user_':user_, "user_posts":user_posts}
    return render(request,'core/user_profile.html',context)

class DelatePost(DeleteView):
    model=Post
    success_url="/"

    def get_queryset(self):
        queryset= super().get_queryset()
        return queryset.filter(author_post_id=self.request.user.id)

class UserList(ListView):
    model=CustomUser
    template_name="core/users.html"

def advanced_serch(request):
    form= SpecificheRicercaForm(request.POST or None)
    ip='95.237.149.43'
    city = from_ip_to_city(ip)
    pointA = from_ip_to_cordinate(ip)
    geolocator= Nominatim(user_agent='measurements')
    posts_in_radius = Post.objects.all()
    if form.is_valid():
        citta_origine_= form.cleaned_data.get('city')
        radius = form.cleaned_data.get('search_radius')
        citta_origine = geolocator.geocode(citta_origine_)
        o_long = citta_origine.longitude
        o_lat = citta_origine.latitude
        pointA = (o_lat,o_long)
        posts=Post.objects.all()
        filtered_dictionary = get_posts_in_radius(radius, posts, pointA)
        posts_in_radius = Post.objects.filter(pk__in= filtered_dictionary.keys() )
    context={"dati":posts_in_radius,'form':form}
    return render(request,"core/advanced_serch.html",context)
