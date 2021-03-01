from django.shortcuts import render, redirect, HttpResponseRedirect
from twitteruser.models import CustomUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    tweet_list = Tweet.objects.all()[::-1]
    context = {'heading': f'Welcome, {request.user.username}!', 'tweet_list': tweet_list}
    return render(request, 'index.html', context)

def profile_view(request, user_name):
    user_info = CustomUser.objects.get(username=user_name)
    tweets = Tweet.objects.filter(post_user=user_info)
    context = {
        'heading': f'The Profile Page of {user_info.display_name}',
        'user': user_info,
        'tweets': tweets
        }
    return render(request, 'user_page.html', context)