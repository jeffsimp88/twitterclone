from django.db import models
from django.conf import settings
from tweet.models import Tweet
from twitteruser.models import CustomUser

class Notification(models.Model):
    tag_user = models.ForeignKey(CustomUser, related_name = 'tag_user', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    is_viewed = models.BooleanField(default=False)
    def __str__(self):
        return f'Notification from {self.tweet.post_user} | {tweet.message}'

