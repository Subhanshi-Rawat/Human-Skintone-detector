from django.db import models
from numpy.lib.type_check import imag
from . import views

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.base import Model
from . import managers


class Fileupload(models.Model):
    fileupload = models.FileField()
    file_id = models.CharField(max_length=20,primary_key=True)
    objects=managers.fileuploaddetails_manager()

