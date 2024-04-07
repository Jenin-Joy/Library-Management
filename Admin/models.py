from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_contact = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=30)

class tbl_district(models.Model):
    district_name = models.CharField(max_length=30)

class tbl_place(models.Model):
    district = models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name = models.CharField(max_length=30)

# class tbl_type(models.Model):
#     type_name = models.CharField(max_length=30)

class tbl_staff(models.Model):
    staff_name = models.CharField(max_length=30)
    staff_contact = models.CharField(max_length=30)
    staff_email = models.CharField(max_length=30)
    staff_address = models.CharField(max_length=30)
    staff_photo = models.FileField(upload_to="Assets/Staff/")
    staff_password = models.CharField(max_length=30)

class tbl_document(models.Model):
    document_name = models.CharField(max_length=30)
    document_description = models.CharField(max_length=30)
    document_image = models.FileField(upload_to='Assets/Documents/')