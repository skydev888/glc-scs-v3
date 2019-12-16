from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile


# signup form
class UserCreateForm(UserCreationForm):
        username = forms.CharField(max_length=130, required=True , label="Username")
        password1 = forms.CharField(widget=forms.PasswordInput(),label="Password")
        password2 = forms.CharField(widget=forms.PasswordInput(),label="Password(Confirm)")
        phone = forms.CharField(max_length=30, required=True , label="Phone number")

        class Meta:
            model = User
            fields = ("username", "password1", "password2", "phone")


# eidt form TEST
class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""
    class Meta:
        model = UserProfile
        fields = ("password1", "password2", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'