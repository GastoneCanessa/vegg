from django.shortcuts import render,HttpResponseRedirect
from  django.contrib.auth import authenticate,login
from .models import CustomUser
from users.forms import FormRegistrazione

def registrazione_view(request):
    if request.method == 'POST':
     form= FormRegistrazione(request.POST)
     if form.is_valid():
         username = form.cleaned_data['username']
         email = form.cleaned_data['email']
         city=form.cleaned_data['city']
         address = form.cleaned_data['address']
         district = form.cleaned_data['district']
         postal_code = form.cleaned_data['postal_code']
         password = form.cleaned_data['password1']
         CustomUser.objects.create_user(
             username=username,
             password=password,
             email=email,
             city=city,
             address=address,
             district=district,
             postal_code=postal_code,
         )
         user = authenticate(username=username, password=password,)
         login(request, user)
         return HttpResponseRedirect('/')
    else:
        form=FormRegistrazione()
        context = {"form":form}
        return render(request, "users/registrazione.html",context)
