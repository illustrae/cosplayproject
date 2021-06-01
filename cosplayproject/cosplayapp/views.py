from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def home(request):
    return render(request, 'index.html')

def login(request):
    user = User.objects.filter(userName = request.POST['username'])
    if user:
        userName = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userName.password.encode()):
            request.session['user_id'] = userName.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'The username is not in our system, please register for an account')
    return redirect('/')

def register(request):
    return render(request, 'registration.html')

def newUser(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('register')
    hashedPW = bcrypt.hashpw(request.POST['password'].eencode(), bcrypt.gensalt()).decode()
    newUser.objects.create(
        username = request.POST['username'],
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashedPW,
        confirm_pw = hashedPW,
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')