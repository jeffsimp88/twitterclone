from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    display_name = models.CharField( max_length=50, null=True, blank=True)
    email = models.EmailField( max_length=254, null=True, blank=True)
    following_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_following', blank=True)
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
