from django.contrib import admin
from .models import suggest_hospital
from .models import Item
from .models import Physio
from .models import Feedback
from .models import Book
from .models import Hospital
from .models import Doctors
from embed_video.admin import AdminVideoMixin
# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(suggest_hospital)
admin.site.register(Item, MyModelAdmin)
admin.site.register(Physio, MyModelAdmin)
admin.site.register(Feedback)
admin.site.register(Book)
admin.site.register(Hospital)
admin.site.register(Doctors)

