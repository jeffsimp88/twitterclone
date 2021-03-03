from django.shortcuts import render
from notifications.models import Notification


def notifications_view(request):
    context = {'heading': 'Notifications!'}
    return render(request, 'notifications.html', context)
