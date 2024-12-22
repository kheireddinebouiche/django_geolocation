from django.urls import path
from . import views

app_name="gps"

urlpatterns = [
    path('', views.map_view, name='map'),
    path('locations/', views.locations_data, name='locations_data'),
]
