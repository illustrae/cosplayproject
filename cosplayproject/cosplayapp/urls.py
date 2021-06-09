from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.newUser),
    path('newUser/', views.users),
    path('userProfile/', views.userProfile),
    path('createProfile/', views.createProfile),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
    

]