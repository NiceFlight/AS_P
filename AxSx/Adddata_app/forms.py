from dataclasses import field
from django import forms
from .models import TempSites


class adddataForm(forms.ModelForm):
    class Meta:
        model = TempSites
        fields = ["name", "type", "description", "year", "latitude", "longitude", "note", "county", "town", "towncode"]
