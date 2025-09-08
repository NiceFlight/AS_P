from django.contrib import admin
from Routes_app.models import AirportsData


# Register your models here.
class showAirports(admin.ModelAdmin):
    list_display = ["name", "lat", "lng", "iata_code", "country", "city"]


admin.site.register(AirportsData, showAirports)
