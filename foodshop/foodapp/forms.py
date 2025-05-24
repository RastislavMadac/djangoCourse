from django import forms 

from django.contrib.auth.models import User 

from django.contrib.auth.forms import UserCreationForm 

 
 

 
 

class CustomUserCreationForm(UserCreationForm): 

    #je tam username password1 pasword2  a overuje ci su rovnake

    email = forms.EmailField(required=True) 

 
 

    class Meta: 
        # vnorena trieda pouziva sa vo formulenach a modeloch na stavuje pravidla  ake policka ma zobrazit
        model = User 

        fields = ['username', 'email', 'password1', 'password2'] 

 
 