from Axsx_app import views
from django.urls import path


urlpatterns = [path("api/views_AxSx/", views.view_AxSx, name="view_AxSx")]
