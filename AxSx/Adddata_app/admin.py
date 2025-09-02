from django.contrib import admin
from .models import TempSites

class showTemp(admin.ModelAdmin):
    list_display = ('name', 'type', 'latitude', 'longitude')
admin.site.register(TempSites, showTemp)
