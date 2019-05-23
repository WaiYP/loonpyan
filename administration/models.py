from datetime import datetime
from django.db import models


class LearningPagePicture(models.Model):
    description = models.CharField(max_length=300)
    photo_1 = models.FileField(upload_to='learning_images', null=True)
    photo_2 = models.FileField(upload_to='learning_images', null=True)
    photo_3 = models.FileField(upload_to='learning_images', null=True)
    photo_4 = models.FileField(upload_to='learning_images', null=True)
    photo_5 = models.FileField(upload_to='learning_images', null=True)
    photo_6 = models.FileField(upload_to='learning_images', null=True)
    rsrv_char_field_1 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_char_field_2 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_photo_field_1 = models.FileField(upload_to='learning_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='learning_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='learning_images', null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.description

class AboutPagePicture(models.Model):
    description = models.CharField(max_length=300)
    photo_1 = models.FileField(upload_to='about_images', null=True)
    photo_2 = models.FileField(upload_to='about_images', null=True)
    photo_3 = models.FileField(upload_to='about_images', null=True)
    rsrv_char_field_1 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_char_field_2 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_photo_field_1 = models.FileField(upload_to='about_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='about_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='about_images', null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.description

