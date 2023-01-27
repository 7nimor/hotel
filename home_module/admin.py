from django.contrib import admin
from . import models


# Register your models here.
class listview(admin.ModelAdmin):
    list_display = ['room','date_in', 'date_out']


admin.site.register(models.HotelRoom)
admin.site.register(models.DetailRoom)
admin.site.register(models.Reserved,listview)
