from  django import  forms

class  ResearchFormMap(forms.Form):
    city=forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter the city from which you want to start the search.'}))
    position= forms.BooleanField(required=False, initial=False, label=' Select to start from your location.')
    search_radius=forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the radius for your search.'}))
