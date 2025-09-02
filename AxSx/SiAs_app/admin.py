from django.contrib import admin
from .models import SinicaArchaeologySites


class showSiAs(admin.ModelAdmin):
    list_display = ("id", "name", "code", "des", "era", "culture_type", "rating", "year", "city", "town", "lat", "lng")


admin.site.register(SinicaArchaeologySites, showSiAs)
