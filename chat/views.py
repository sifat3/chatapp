from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            messages.success("Login successful!")
            return redirect('home')
        else:
            messages.success('Invalid Username or Password, Please Try Again.')
            return redirect('home')


    return render(request, 'chat/home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'chat/signup.html')


