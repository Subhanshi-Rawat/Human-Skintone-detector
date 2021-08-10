from django.db import models
from django.db.models.base import Model
from django.db.models.manager import Manager

class fileuploaddetails_manager(models.Manager):
    def create_fileupload(self,file_id,fileupload):
        fileupload_details = self.create(file_id=file_id,fileupload=fileupload)
        return fileupload_details
