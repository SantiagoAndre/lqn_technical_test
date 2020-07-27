from django import forms
from .models import *


class CreateCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields ="__all__"

class CreatePlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields ="__all__"

class CreateProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields ="__all__"

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields ="__all__"