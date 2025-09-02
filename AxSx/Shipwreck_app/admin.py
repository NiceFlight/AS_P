from django.contrib import admin
from Shipwreck_app.models import ShipWreck

# Register your models here.
class showShipwreck(admin.ModelAdmin):
    list_display = ['shipwreckno','name', 'latitude', 'longitude', 'sinkyear']
admin.site.register(ShipWreck, showShipwreck)