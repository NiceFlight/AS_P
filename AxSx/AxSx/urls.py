"""
URL configuration for AxSx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
import Routes_app.views
import Shipwreck_app.views
import Adddata_app.views
import Addsites_app.views
import Addsitesalert_app.views
import Circuits_app.views
import SiAs_app.views
import Geolocation_app.views
import Axsx_app.views
import ASList_app.views
import maplibre_app.views
from django.views.generic import RedirectView

app_name = "axsx"

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url="/static/img/favicon.ico")),  # 設定標籤小圖示
    path("admin/", admin.site.urls, name="admin"),
    path("", Axsx_app.views.Axsx, name=""),
    # path("view_AxSx/", Map_app.views.view_AxSx, name="view_AxSx"),
    path("", include("Axsx_app.urls")),
    path("adddata/", Adddata_app.views.adddata, name="adddata"),
    path("adddata/added/", Adddata_app.views.adddata, name="added"),
    path("addsites/", Addsites_app.views.addsites, name="addsites"),
    path("addsites/sitesadded/", Addsites_app.views.addsites, name="sitesadded"),
    path("addsitesalert/", Addsitesalert_app.views.addsitesalert, name="addsitesalert"),
    path("routesmap/", Routes_app.views.routesmap, name="routesmap"),
    path("routesmap/updatedestination/", Routes_app.views.updateDestination, name="updatedestination"),
    path("api/routesmap_json/", Routes_app.views.routesmap_json, name="routesmap_json"),
    path("shipwreck/", Shipwreck_app.views.shipwreck, name="shipwreck"),
    path("api/circuits_json/", Circuits_app.views.circuits_json, name="circuits"),
    path("circuits/", Circuits_app.views.circuits, name="circuits"),
    path("sias/", SiAs_app.views.sias, name="sias"),
    path("api/sias_json/", SiAs_app.views.view_sias, name="view_sias"),
    path("geolocation/", Geolocation_app.views.geolocation, name="geolocation"),
    path("aslist/", ASList_app.views.ASList, name="aslist"),
    path("maplibre/", maplibre_app.views.maplibre_app, name="maplibre"),
    path("api/view_maplibre/", maplibre_app.views.view_maplibre, name="view_maplibre"),
]
