from django import forms
from .models import Menu


class VoteForm(forms.Form):
    day = forms.DateField(widget=forms.SelectDateWidget())
    menu = forms.ModelChoiceField(queryset=Menu.objects.all())
