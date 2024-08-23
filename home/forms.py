# home/forms.py

from django import forms
from .models import Reviews
 # Import your Review model

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
     # Import timezone from django.utils
        fields = ['name', 'comment']
# forms.py
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):  # Fix the typo here
    class Meta:
        model = UserRegistration
        fields = ['name', 'class1']

