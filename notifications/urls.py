from django.urls import path

from notifications import views

urlpatterns = [
    path("notifications/", views.notifications_view, name="notifications"),
    path("notifications/old", views.old_notification_view, name="old notifications"),
]