import requests
from django.shortcuts import render
import ipapi

def base64view(request):
    return render(request, 'base64.html', context)


