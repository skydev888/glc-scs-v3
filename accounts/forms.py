from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# Singup form
class UserCreateForm(UserCreationForm):
        username = forms.CharField(max_length=130, required=True , label="Your Username")
        password1 = forms.CharField(widget=forms.PasswordInput(),label="Your Password")
        password2 = forms.CharField(widget=forms.PasswordInput(),label="Repeat Your Password")
        email = forms.EmailField(max_length=130, required=True ,label="Email Address")
        age = forms.IntegerField(label="Age")
        first_name = forms.CharField(max_length=130, required=True ,label="Name")
        last_name = forms.CharField(max_length=130, required=True ,label="Surname")
        degree = forms.CharField(max_length=130, required=True ,label="Degree name")
        city = forms.CharField(max_length=130, required=True ,label="City")
        state = forms.CharField(max_length=130, required=True ,label="State")
        country = forms.CharField(max_length=130, required=True ,label="Country")

        class Meta:
            model = User
            fields = ("first_name", "last_name", "email", "username", "password1", "password2", "degree", "city",
                      "state", "country", "age")


