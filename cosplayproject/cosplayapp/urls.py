from django.contrib.admin.sites import AdminSite
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
]