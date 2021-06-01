from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.newUser),
    path('newUser/', views.users),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
    

]