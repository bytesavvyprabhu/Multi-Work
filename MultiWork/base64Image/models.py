from django.db import models

class Uploadimage(models.Model):
    image = models.ImageField(blank= True , null= True,upload_to='base64images')