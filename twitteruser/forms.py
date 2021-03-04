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
