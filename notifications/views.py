from django.shortcuts import render
from notifications.models import Notification
from twitteruser.models import CustomUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
import re

def filter_notifications(request, notifications):
    new_list = []
    tweet_list = Tweet.objects.all()
    notify_list = notifications
    for tweet in tweet_list:
        if tweet.id in notify_list:
            new_list.append(tweet)
    return new_list

def check_notifications(user):
    notifications = Notification.objects.filter(tag_user=user).filter(is_viewed=False)
    return notifications
    # notifications = check_notifications(request.user)


def create_notification(tweet):
    tweet_list = Tweet.objects.all()
    user_list = CustomUser.objects.all()
    if '@' in tweet.message:
        tagged_user = re.findall(r'@(\w+)\b', tweet.message)
        for user in tagged_user:
            for username in user_list:
                if user == username.username:
                    Notification.objects.create(
                        tweet = tweet,
                        tag_user=CustomUser.objects.get(username=user)
                    )

@login_required
def notifications_view(request):
    context = {'heading': 'Notifications!'}
    current_user = request.user
    new_notifications = Notification.objects.filter(tag_user=current_user).filter(is_viewed=False)
    
    tweets = filter_notifications(request, new_notifications)
    for notify in new_notifications:
        notify.is_viewed = True
        notify.save()
    context.update({
        'new_notifications': new_notifications, 
        'tweets': tweets, 
        'user': current_user
        })
    return render(request, 'notifications.html', context)

@login_required
def old_notification_view(request):
    context = {'heading': 'Old Notifications!'}
    notifications = check_notifications(request.user)
    current_user = request.user
    new_notifications = Notification.objects.filter(tag_user=current_user).filter(is_viewed=True)
    tweets = filter_notifications(request, new_notifications)
    context.update({
        'new_notifications': new_notifications,
        'notifications': notifications, 
        'tweets': tweets, 
        'user': current_user
        })
    return render(request, 'notifications.html', context)
