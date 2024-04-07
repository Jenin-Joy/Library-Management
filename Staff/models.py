from django.db import models
from Admin.models import *
# Create your models here.
class tbl_book(models.Model):
    book_name = models.CharField(max_length=30)
    book_author = models.CharField(max_length=30)
    book_publisher = models.CharField(max_length=30)
    book_description = models.CharField(max_length=100)
    book_image = models.FileField(upload_to='Assets/book_images/')
    book_price = models.IntegerField()
    book_status = models.IntegerField(default=0)
    category = models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    staff = models.ForeignKey(tbl_staff,on_delete=models.CASCADE)

class tbl_journal(models.Model):
    journal_name = models.CharField(max_length=30)
    journal_volume = models.CharField(max_length=30)
    journal_publisher = models.CharField(max_length=30)
    journal_topic = models.CharField(max_length=50)
    journal_image = models.FileField(upload_to='Assets/journal_images/')
    journal_price = models.IntegerField()
    journal_status = models.IntegerField(default=0)
    staff = models.ForeignKey(tbl_staff,on_delete=models.CASCADE)