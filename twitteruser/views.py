from django.shortcuts import render, redirect, HttpResponseRedirect
from twitteruser.models import CustomUser
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    users_list = CustomUser.objects.all()
    context = {'heading': f'Welcome, {request.user.username}!', 'users_list': users_list}
    return render(request, 'index.html', context)