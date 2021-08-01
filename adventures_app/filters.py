from django import forms
import django_filters
from django_filters.filters import ModelMultipleChoiceFilter
from .models import *

class TripFilter(django_filters.FilterSet): 
    category=ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.widgets.CheckboxSelectMultiple
        )
    class Meta:
        model = Trip
        fields = ['guide','category']
    