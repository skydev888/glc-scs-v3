from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# signup form
class UserCreateForm(UserCreationForm):
        username = forms.CharField(max_length=130, required=True , label="Username")
        password1 = forms.CharField(widget=forms.PasswordInput(),label="Password")
        password2 = forms.CharField(widget=forms.PasswordInput(),label="Password(Confirm)")
        password3 = forms.CharField(max_length=130, required=True , label="raw password")
        phone = forms.IntegerField(label="Mobile phone number")

        class Meta:
            model = User
            fields = ("username", "password1", "password2", "password3", "phone")

# edit form
class UserEditForm(forms.Form):
        username = forms.CharField(max_length=130, required=True , label="Username")
        password1 = forms.CharField(widget=forms.PasswordInput(),label="Password")
        password2 = forms.CharField(widget=forms.PasswordInput(),label="Password(Confirm)")
        password3 = forms.CharField(max_length=130, required=True , label="raw password")
        phone = forms.IntegerField(label="Mobile phone number")

        class Meta:
            model = User
            fields = ("username", "password1", "password2", "password3", "phone")