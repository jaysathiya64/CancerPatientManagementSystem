from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('ulogin',views.ulogin,name='ulogin'),
    path('usignup',views.usignup,name='usignup'),
    path('ulogin.html',views.userlogin,name='userlogin'),
    path('usignup.html',views.usersignup,name='usersignup'),
    path('ulogout',views.ulogout,name='ulogout')
]