from django.contrib import admin
from .models import TaiwanArchaeologySites

class showAxSx(admin.ModelAdmin):
    list_display = ('name', 'type', 'latitude', 'longitude')
admin.site.register(TaiwanArchaeologySites, showAxSx)