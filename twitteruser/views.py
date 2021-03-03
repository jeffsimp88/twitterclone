from django.shortcuts import render, redirect, HttpResponseRedirect
from twitteruser.models import CustomUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    tweet_list = Tweet.objects.all()[::-1]
    context = {'heading': f'Welcome, {request.user.username}!', 'tweet_list': tweet_list}
    return render(request, 'index.html', context)

def check_following(request, user_name):
    user_info = CustomUser.objects.get(username=user_name)
    current_user = request.user
    users_following= current_user.following_user
    if users_following.filter(username=user_name).exists():
        is_followed=True
    else:
        is_followed=False
    return is_followed

def profile_view(request, user_name):
    user_info = CustomUser.objects.get(username=user_name)
    tweets = Tweet.objects.filter(post_user=user_info)
    followers = user_info.following_user
    if not followers:
        followers = None
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
    check_follower = get_user.following_user
    is_followed = False
    if other_user.username != request.user:
        if check_follower.filter(username=other_user).exists():
            # remove_follower = Followers.objects.get(user=get_user)
            check_follower.remove(other_user)
            is_followed = False
            return redirect(f'/users/{other_user}')
        else:
            # add_follower = Followers.objects.get(user=get_user)
            check_follower.add(other_user)
            is_followed = True
            return redirect(f'/users/{other_user}')
    else:
        return redirect(f'/users/{request.user}')

