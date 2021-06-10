from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Home Login Page
def home(request):
    return render(request, 'index.html')
# registration form
def newUser(request):
    return render(request, 'registration.html')
# user register form
def users(request):
    if request.method == "GET":
        return redirect('/register')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/register')
    hashedPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        username = request.POST['username'],
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashedPW,
        confirm_pw = hashedPW,
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')
# login validations
def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'The username is not in our system, please register for an account')
    return redirect('/')

def dashboard(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context)

def userProfile(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
    'user': user,
    }
    return render(request, 'profile.html', context)

# log out of application
def logout(request):
    request.session.clear()
    return redirect('/')


