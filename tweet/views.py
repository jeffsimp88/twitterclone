from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetForm

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
            return HttpResponseRedirect('/')
    form = TweetForm()
    context = {'heading': 'Post a Tweet', 'form': form}
    return render(request, 'forms.html', context)

def tweet_view(request, tweet_id):
    context = {'heading': "Tweet Details"}
    tweet = Tweet.objects.get(id=tweet_id)
    context.update({'tweet': tweet})
    return render(request, 'tweet_details.html', context)
    