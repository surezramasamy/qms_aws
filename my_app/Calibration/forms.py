from django import forms
from .models import Fixture_List

CHART_CHOICES = (
    ('#1', 'Bar Graph'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Graph')
)

RESULTS_CHOICES = (
    ('#1', 'Product_description'),
    ('#2', 'Location_used'),
    ('#3', 'Description'),
    ('#4', 'Status')
    )


class calform(forms.Form):
        date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
