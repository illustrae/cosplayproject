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
    path('forum/', views.forum),
    path('wall', views.message),
    path('add_comment/<int:id>', views.comment),
    path('like/<int:id>', views.add_like),
    path('characters/', views.character),
    path('delete/<int:id>', views.delete),
    path('logout/', views.logout),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)