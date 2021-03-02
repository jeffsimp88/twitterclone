from django.shortcuts import render, redirect, HttpResponseRedirect
from twitteruser.models import CustomUser, Followers
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    tweet_list = Tweet.objects.all()[::-1]
    context = {'heading': f'Welcome, {request.user.username}!', 'tweet_list': tweet_list}
    return render(request, 'index.html', context)

def check_following(request, user_name):
    user_info = CustomUser.objects.get(username=user_name)
    session_user = request.user
    session_following= Followers.objects.get(user=session_user)
    following= Followers.objects.get(user=session_user.id)
    if session_following.following_user.filter(username=user_name).exists() or following.following_user.filter(username=user_name).exists():
        is_followed=True
    else:
        is_followed=False
    return is_followed

def profile_view(request, user_name):
    user_info = CustomUser.objects.get(username=user_name)
    tweets = Tweet.objects.filter(post_user=user_info)
    followers = Followers.objects.filter(user=user_info.id)
    if not followers:
        followers = None
    else:
        followers = Followers.objects.get(user=user_info.id)
    if not request.user.is_authenticated:
        context = {
            'heading': f'The Profile Page of {user_info.display_name}',
            'user': user_info,
            'tweets': tweets,
            'followers':followers,
            }
        return render(request, 'user_page.html', context)
    else:
        is_followed = check_following(request, user_name)    
        context = {
            'heading': f'The Profile Page of {user_info.display_name}',
            'user': user_info,
            'tweets': tweets,
            'is_followed': is_followed,
            'followers':followers,
            }
        return render(request, 'user_page.html', context)


def follow_user(request, user_name):
    other_user = CustomUser.objects.get(username=user_name)
    get_user = CustomUser.objects.get(username=request.user)
    check_follower = Followers.objects.get(user=get_user.id)
    is_followed = False
    if other_user.username != request.user:
        if check_follower.following_user.filter(username=other_user).exists():
            remove_follower = Followers.objects.get(user=get_user)
            remove_follower.following_user.remove(other_user)
            is_followed = False
            return redirect(f'/users/{other_user}')
        else:
            add_follower = Followers.objects.get(user=get_user)
            add_follower.following_user.add(other_user)
            is_followed = True
            return redirect(f'/users/{other_user}')
    else:
        return redirect(f'/users/{request.user}')

