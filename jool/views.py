from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from jool.forms import UserForm
from collabo.models import Article


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('jool:index')
    else:
        form = UserForm()
    return render(request, 'login/signup.html', {'form': form})


def about(request):
    return render(request, 'about.html')
