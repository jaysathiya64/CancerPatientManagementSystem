
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appointment.urls')),
    path('',include('hospital1.urls')),
    path('',include('user.urls')),
    path('chat/', include('chat.urls')),
]
