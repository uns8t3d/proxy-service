from django import forms
from .models import Users
from django.contrib.auth.models import User, models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'email',
            'last_name',
            'first_name',
            'password'
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ( 'Username', 'FirstName', 'LastName', 'Email', 'Password')

