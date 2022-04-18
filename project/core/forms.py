from django import forms
from .models import Post
from django.core.validators import RegexValidator

class PostModelForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['image','content']

class  SpecificheRicercaForm(forms.Form):

    city=forms.CharField(validators=[
        RegexValidator(
            regex=r'^[a-zA-Z]',
            message=('City name must be made from Letters'),
        )])
    search_radius=forms.IntegerField()
