from django.contrib import admin
from .models import TaiwanArchaeologySites


class showAxSx(admin.ModelAdmin):
    list_display = ("name", "culture_type", "lat", "lng")


admin.site.register(TaiwanArchaeologySites, showAxSx)
