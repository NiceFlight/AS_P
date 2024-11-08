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
from django.urls import path
import Hub_app.views
import Shipwreck_app.views
import Map_app.views
import Adddata_app.views
import Addsites_app.views
import Addsitesalert_app.views
import Circuits_app.views
from django.views.generic import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),  # 設定標籤小圖示方法
    path('admin/', admin.site.urls, name="admin"),
    path('', Map_app.views.map, name=""), 
    path('view_AxSx/', Map_app.views.view_AxSx, name="view_AxSx"),
    # path('adddata/', Adddata_app.views.adddata, name="adddata"), 
    path('adddata/', Adddata_app.views.adddata, name="adddata"), 
    path('adddata/added/', Adddata_app.views.adddata, name="added"), 
    path('addsites/', Addsites_app.views.addsites, name='addsites'), 
    path('addsites/sitesadded/', Addsites_app.views.addsites, name='sitesadded'), 
    # path('addsites/sitesadded/', Addsites_app.views.sitesadded, name='sitesadded'), 
    path('addsitesalert/', Addsitesalert_app.views.addsitesalert, name='addsitesalert'), 
    path('hubmap/', Hub_app.views.hubmap, name="hubmap"), 
    path('shipwreck/', Shipwreck_app.views.shipwreck, name="shipwreck"), 
    path('circuits_json/', Circuits_app.views.circuits_json, name="circuits"), 
    path('circuits/', Circuits_app.views.circuits, name="circuits"), 
]