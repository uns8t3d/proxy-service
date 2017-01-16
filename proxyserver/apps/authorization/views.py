from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    return render(request, 'authorization/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

