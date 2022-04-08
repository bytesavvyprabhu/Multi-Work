from django.urls import path
from .views import ip_based_location

urlpatterns = [
    path('', ip_based_location, name = 'index'),

]