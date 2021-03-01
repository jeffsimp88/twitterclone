from django.urls import path
from twitteruser import views


urlpatterns = [
    path('', views.index_view, name='homepage'),
]