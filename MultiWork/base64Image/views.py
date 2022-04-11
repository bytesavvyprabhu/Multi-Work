from django.shortcuts import redirect, render
import base64 , os
from .forms import UserImageForm
from .models import Uploadimage
def Index(request):
    return render(request, 'base64.html')
def Upload(request):
    pic = request.FILES['Image']
    a=Uploadimage()
    a.image=pic
    a.save()
    b = "C:/Users/pds/PycharmProjects/Multi-Work/MultiWork/media/base64images/"
    path = os.path.join(b,str(pic))
    with open(path, "rb") as img_file:
        data = base64.b64encode(img_file.read())
    print(request.FILES)
    context = {"data":data}
    os.remove(path)
    return render(request, 'base64.html',context)