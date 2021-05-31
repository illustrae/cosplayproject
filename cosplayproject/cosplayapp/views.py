from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def home(request):
    return render(request, 'index.html')


def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        userEmail = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userEmail.password.encode()):
            request.session['user_id'] = userEmail.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'The email is not in our system, please register for an account')
    return redirect('/')
