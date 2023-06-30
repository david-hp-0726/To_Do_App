from django.contrib.auth.models import User
from django import forms
from .models import List
from django.contrib.auth.forms import UserCreationForm

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["title", "description", "priority"]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
