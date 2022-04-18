from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class FormRegistrazione(UserCreationForm):
    email = forms.CharField(max_length=30 ,required=True ,widget=forms.EmailInput())
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)
    district = forms.CharField(required=True)
    postal_code = forms.IntegerField(required=True)

    class Meta:
        model= CustomUser
        fields=['username','email','city','address','district','postal_code','password1','password2']
