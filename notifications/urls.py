from django.urls import path

from notifications import views

urlpatterns = [
    path("notifications/", views.notifications_view, name="notifications"),
]