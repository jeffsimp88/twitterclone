from django.shortcuts import render, redirect, HttpResponseRedirect
from twitteruser.models import CustomUser
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    context = {'heading': f'Welcome, {request.user.username}!'}
    return render(request, 'index.html', context)