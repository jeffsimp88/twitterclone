from django.urls import path
from twitteruser import views


urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('users/<user_name>/', views.profile_view, name='profile page'),
    path('follow/<str:user_name>', views.follow_user, name='follow'),
    path('recenttweets/', views.recent_tweets_view, name='recent tweets')
]