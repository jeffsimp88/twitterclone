from django.urls import path
from tweet import views


urlpatterns = [
    path('posttweet/', views.post_tweet_view, name='post tweet'),
]