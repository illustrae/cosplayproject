from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.newUser),
    path('newUser/', views.users),
    path('editProfile/<int:user_id>/updateProfile', views.updateProfile),
    path('editProfile/', views.editProfile),
    path('userProfile/', views.userProfile ),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)