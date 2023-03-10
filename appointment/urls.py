from django.urls import path
from . import views

urlpatterns = [
    path('bookap',views.bookap,name='appointment'),
    path('sfeedback',views.sfeedback,name='give_feedback'),
    path('seeappointment',views.seeappointment,name='seeappointment')
]