from django.urls import path
from tweet import views


urlpatterns = [
    path('posttweet/', views.post_tweet_view, name='post tweet'),
    path('tweet/<int:tweet_id>/', views.tweet_view, name="tweet details"),
    path('deletetweet/<int:tweet_id>/', views.delete_tweet_view, name="delete tweet")
]