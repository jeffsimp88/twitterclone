from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import CustomUser
from notifications.models import Notification
from notifications.views import check_notifications, create_notification


@login_required
def post_tweet_view(request):
    if request.method =='POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                message=data['message'],
                post_user = request.user
            )
            create_notification(new_tweet)
            return HttpResponseRedirect('/')
    form = TweetForm()
    notifications = check_notifications(request.user)
    context = {'heading': 'Post a Tweet', 'form': form, 'notifications': notifications}
    return render(request, 'forms.html', context)

def tweet_view(request, tweet_id):
    notifications = ''
    if request.user.is_authenticated:
        notifications = check_notifications(request.user)
    context = {'heading': "Tweet Details", 'notifications': notifications}
    tweet = Tweet.objects.get(id=tweet_id)
    context.update({'tweet': tweet})
    return render(request, 'tweet_details.html', context)
    
def delete_tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')