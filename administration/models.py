from datetime import datetime
from django.db import models


class LearningPagePicture(models.Model):
    description = models.TextField(null=True, blank=True)
    photo_1 = models.FileField(upload_to='learning_images', null=True)
    photo_2 = models.FileField(upload_to='learning_images', null=True)
    photo_3 = models.FileField(upload_to='learning_images', null=True)
    photo_4 = models.FileField(upload_to='learning_images', null=True)
    photo_5 = models.FileField(upload_to='learning_images', null=True)
    photo_6 = models.FileField(upload_to='learning_images', null=True)
    description2 = models.TextField(null=True,blank=True)
    description3 = models.TextField(null=True, blank=True)
    description4 = models.TextField(null=True, blank=True)
    description5 = models.TextField(null=True, blank=True)
    description6 = models.TextField(null=True, blank=True)
    rsrv_char_field_1 = models.TextField(null=True, blank=True)
    rsrv_char_field_2 = models.TextField(null=True, blank=True)
    rsrv_photo_field_1 = models.FileField(upload_to='learning_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='learning_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='learning_images', null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.description

class AboutPagePicture(models.Model):
    description = models.TextField(null=True, blank=True)
    photo_1 = models.FileField(upload_to='about_images', null=True)
    photo_2 = models.FileField(upload_to='about_images', null=True)
    photo_3 = models.FileField(upload_to='about_images', null=True)
    rsrv_char_field_1 = models.TextField(null=True, blank=True)
    rsrv_char_field_2 = models.TextField(null=True, blank=True)
    rsrv_photo_field_1 = models.FileField(upload_to='about_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='about_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='about_images', null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.description

