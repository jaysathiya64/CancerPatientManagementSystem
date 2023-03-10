from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('hlogin',views.hlogin,name='hlogin'),
    path('hsignup',views.hsignup,name='hsignup'),
    path('signup.html',views.signup,name='signup'),
    path('adddoctor.html',views.adddoctor,name='adddoctor'),
    path('doctorlogin',views.doctorlogin,name='dlogin'),
    path('registerdoctor',views.registerdoctor,name='registerdoctor'),
    path('registerdoctor/<int:d_id>',views.remove,name='removedoctor'),
    path('mainhome',views.home,name='listofap'),
    path('cancel/<int:ap_id>',views.cancel,name='cancel'),
    path('cancelap/<int:ap_id>',views.cancelap,name='cancelap'),
    path('hlogout',views.hlogout,name='hlogout'),  
    path('dlogout',views.dlogout,name='dlogout')
]