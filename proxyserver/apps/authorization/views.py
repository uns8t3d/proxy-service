from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import forms
from .models import Users
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import PostForm
from django.shortcuts import redirect



def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('core:dashboard'))
        else:
            return HttpResponseRedirect(reverse('auth:login'))
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth:login'))


def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = forms.EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()
    return render(request, 'contact.html', {'form': form})


def users(request):
    return render_to_response('users.html', {'users': Users.objects.all()})


