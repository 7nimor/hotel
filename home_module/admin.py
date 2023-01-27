from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.HotelRoom)
admin.site.register(models.DetailRoom)
admin.site.register(models.Reserved)