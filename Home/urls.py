from django.contrib import admin
from django.urls import path
from . import views
#from .views import video

urlpatterns = [
    path('', views.index , name='index'),
    path('diet', views.diet , name='diet_plan'),
    path('bookapp', views.bookapp , name='book_appointment'),
    path('deleteapp/<int:ap_id>', views.deleteapp , name='delete_appointment'),
    path('myapp', views.seeapp , name='see_appointment'),
    path('physio', views.physio , name='physiotherapy'),
    path('givefeedback', views.userfeedback , name='feedback'),
    path('hospital_login', views.hospital_login , name='hospital_login'),
    path('hospital_home', views.hospital_home , name='hospital_home'),
    path('payment', views.payment , name='payment')
]