from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [

    path('register', views.userRegister, name='user_register'),
    path('register/create', views.userCreate, name='user_create'),

    path('login', views.loginView, name='login'),
    path('login/create ', views.loginCreate, name='login_create'),
    path('logout/', views.logoutUser, name='logout_user'),
]
