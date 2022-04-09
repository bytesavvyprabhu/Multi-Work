from django.shortcuts import redirect, render
import base64
from .forms import UserImageForm
from .models import Uploadimage
def Index(request):
    return render(request, 'base64.html')
def Upload(request):
    pic = request.FILES['Image']
    b = 0
    a=Uploadimage()
    a.image=pic
    a.save()
    with open(pic, "rb") as img_file:
        b = base64.b64encode(img_file.read())
    context = {"data": b}
    print(request.FILES)
    return render(request, 'base64.html', context)