from django.db import models
from django.conf import settings
from django.utils import timezone

class Tweet(models.Model):
    message = models.TextField(max_length=140)
    date_posted = models.DateTimeField(default=timezone.now)
    post_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'post_user'
        )
    def __str__(self):
        return f'{self.message} | {self.post_user}'
