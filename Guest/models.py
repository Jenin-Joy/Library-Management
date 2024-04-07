from django.db import models
from Admin.models import *
# Create your models here.

class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_contact = models.CharField(max_length=10)
    user_email = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    user_photo = models.FileField(upload_to='Assets/user_photo/')
    user_doj = models.DateField(auto_now_add=True)
    user_status = models.IntegerField(default=0)
    user_password = models.CharField(max_length=30)
    types = models.IntegerField()
    place = models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_content = models.CharField(max_length=500)
    complaint_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint_reply = models.CharField(max_length=500)
    complaint_status = models.IntegerField(default=0)