from django.shortcuts import render
import ipapi

def ip_based_location(request):
    a= request.POST.get('search')
    data = ipapi.location(ip=a, output='json')
    context = {"data":data}
    return render(request, 'iploction.html', context)
