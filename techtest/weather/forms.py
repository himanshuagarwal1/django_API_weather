from django import forms

class GetTemperatureInfo(forms.Form):
    languages = (("en", "English"), ("de", "German"), ("fr", "French"))
    city_name = forms.CharField(label= "City Name", max_length=50)
    lang = forms.ChoiceField(label= "Language", choices=languages, widget= forms.RadioSelect)