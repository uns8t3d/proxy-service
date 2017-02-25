from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


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

