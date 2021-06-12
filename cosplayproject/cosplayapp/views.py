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

#shows the home and dashboard of all users
def dashboard(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context)

#loads a user profile.
def userProfile(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
    'user': user,
    }
    return render(request, 'profile.html', context)

#edit user profile
def editProfile(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
    'user': user,
    }
    return render(request, 'editProfile.html', context)

# updates edited information on profile and updates new image photo.
def updateProfile(request, user_id):
    userProfile = User.objects.get(id=request.session['user_id'])
    userProfile.profile.location = request.POST['location']
    userProfile.profile.favorite = request.POST['favorite']
    userProfile.profile.about = request.POST['about']
    userProfile.profile.image = request.FILES['image']
    userProfile.save()

    return redirect(f'/userProfile')
#forum wall view
def forum(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'messages': Message.objects.all()
    }
    return render(request, 'forum.html', context)
#post wall messages
def message(request):
    Message.objects.create(message = request.POST['mess'], poster = User.objects.get(id=request.session['user_id']))
    return redirect('/forum/')
#post comments
def comment(request, id):
    poster = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/forum/')

def add_like(request, id):
    liked_message = Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)

    return redirect('/forum/')

def delete(redirect, id):
    destroyed = Comment.objects.get(id=id)
    destroyed.delete()
    return redirect('/forum/')

def character(request):
    if 'user_id' not in  request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'characters.html', context)
# log out of application
def logout(request):
    request.session.clear()
    return redirect('/')


