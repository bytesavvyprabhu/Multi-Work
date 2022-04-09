from django.urls import path, include
from .views import Index, Upload

urlpatterns = [
    path('', Index, name='base64'),
    path('Upload', Upload, name='Upload')
    ]