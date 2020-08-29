from django import forms
from webapp.models import Pol, Choice


class PolForm(forms.ModelForm):
    class Meta:
        model = Pol
        exclude = []


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['Option_text']
