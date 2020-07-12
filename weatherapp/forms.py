from django import forms

class weatherform(forms.Form):
    name=forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={'placeholder':'Find your location...'}))


