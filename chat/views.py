from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.success(request, 'Invalid Username or Password, Please Try Again.')
            return redirect('home')
    
    if request.user.is_authenticated:
        if Chat.objects.filter(users=request.user).exists():
            chats = Chat.objects.filter(users=request.user)
        else:
            chats = []
    else:
            chats = []
    context = {
        'chats': chats,
    }


    return render(request, 'chat/home.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.success(request, "Username taken.")
        else:
            if password1 == password2:
                user = User.objects.create(username=username, password=password1, email=email)
                user.save()
                login(request, user)
                messages.success(request, f'Account Created Successfully. Welcome {username}')
                return redirect('home')
            else:
                messages.success(request, "Passwords don't match")
    return render(request, 'chat/signup.html')


@login_required(login_url='home')
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('home')


@login_required(login_url='home')
def inbox_view(request):
    if Chat.objects.filter(inbox=inbox).exists():
        chats = Chat.objects.filter(inbox=inbox)
    else:
        chats = []
    context = {
        'chats': chats
    }
    return render(request, 'chat/inbox.html', context)



@login_required(login_url='home')
def chat_view(request, pk):
    chat = Chat.objects.get(sender=request.user, reciever=User.objects.get(id=pk))
    messages = chat.message.all()
    context = {
        'body_messages': messages,
        'chat': chat
    }
    return render(request, 'chat/chat.html', context)