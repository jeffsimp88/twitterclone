from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from twitteruser.models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'display_name', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'display_name', 'email',)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    display_name= forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)