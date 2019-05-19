from datetime import datetime
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # path = 'images/{0}/{1}'.format(datetime.now().strftime('%Y/%m/%d'), filename)
    # if Storage.exists(path):
    #     path = Storage.get_available_name(path)
    temp_path = 'product_photo_{0}/{1}'.format(datetime.now().strftime('%Y/%m/%d'), filename)
    return temp_path

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    rsrv_char_field_1 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_char_field_2 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_char_field_3 = models.CharField(max_length=80,blank=True, null=True)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    cat = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

class ProductSubGroup(models.Model):
    pgroup = models.ForeignKey(ProductGroup, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    cat = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    pgroup = models.ForeignKey(ProductGroup, on_delete=models.SET_NULL, null=True, blank=True)
    psubgroup = models.ForeignKey(ProductSubGroup, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    std_cert = models.CharField(max_length=100)
    made_in = models.CharField(max_length=100)
    pdf_doc = models.FileField(max_length=100)
    technology = models.CharField(max_length=100)
    photo_1 =models.FileField(upload_to=user_directory_path, null=True, blank=True)
    photo_2 = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    photo_3 = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    photo_4 = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    photo_5 = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_photo_field_1 = models.FileField(upload_to='bus_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='bus_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='bus_images', null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

class ActivityGroup(models.Model):
    name = models.CharField(max_length=100)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Activities(models.Model):
    agroup = models.ForeignKey(ActivityGroup, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    photo_1 = models.FileField(upload_to='bus_images', null=True)
    photo_2 = models.FileField(upload_to='bus_images', null=True)
    photo_3 = models.FileField(upload_to='bus_images', null=True)
    photo_4 = models.FileField(upload_to='bus_images', null=True)
    photo_5 = models.FileField(upload_to='bus_images', null=True)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_photo_field_1 = models.FileField(upload_to='bus_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='bus_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='bus_images', null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceGroup(models.Model):
    name = models.CharField(max_length=100)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    sgroup = models.ForeignKey(ServiceGroup, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    photo_1 = models.FileField(upload_to='bus_images', null=True)
    photo_2 = models.FileField(upload_to='bus_images', null=True)
    photo_3 = models.FileField(upload_to='bus_images', null=True)
    photo_4 = models.FileField(upload_to='bus_images', null=True)
    photo_5 = models.FileField(upload_to='bus_images', null=True)
    rsrv_char_field_1 = models.CharField(max_length=80)
    rsrv_char_field_2 = models.CharField(max_length=80)
    rsrv_char_field_3 = models.CharField(max_length=80)
    rsrv_no_field_1 = models.IntegerField(null=True)
    rsrv_no_field_2 = models.IntegerField(null=True)
    rsrv_no_field_3 = models.IntegerField(null=True)
    rsrv_photo_field_1 = models.FileField(upload_to='bus_images', null=True)
    rsrv_photo_field_2 = models.FileField(upload_to='bus_images', null=True)
    rsrv_photo_field_3 = models.FileField(upload_to='bus_images', null=True)
    rsrv_date_field_1 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_2 = models.DateTimeField(blank=True, null=True)
    rsrv_date_field_3 = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ts = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
