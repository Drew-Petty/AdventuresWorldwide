from django import forms
from django.forms import ModelForm, widgets
from allauth.account.forms import SignupForm
from .models import Category, Trip


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    
class PictureForm(forms.Form):
    picture = forms.ImageField(required=False)

class TripForm(ModelForm):

    class Meta:
        model = Trip
        fields = ['name','duration','cost','capacity','picture']
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple)

class TripEditForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name','duration','cost','capacity','category']
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple)

