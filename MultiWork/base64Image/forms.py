from django.db import models
from django.forms import fields
from .models import Uploadimage
from django import forms


class UserImageForm(forms.ModelForm):
    class meta:
        # To specify the model to be used to create form
        models = Uploadimage
        # It includes all the fields of model
        fields = '__all__'