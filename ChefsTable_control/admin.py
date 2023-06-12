from django.contrib import admin
from .models import Reservation,Cuisine, Menu

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Cuisine)
admin.site.register(Menu)

