from django.urls import path, include
from . import views

urlpatterns = [
    path('base_64/', views.base64view , name='base64'),
    ]