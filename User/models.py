from django.db import models
from Guest.models import *
from Staff.models import *
# Create your models here.

class tbl_book_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    collected_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    returned_date = models.DateField(null=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    book = models.ForeignKey(tbl_book, on_delete=models.CASCADE)
    booking_status = models.IntegerField(default=0)
    booking_amount = models.IntegerField(default=0)

class tbl_journal_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    collected_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    returned_date = models.DateField(null=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    journal = models.ForeignKey(tbl_journal, on_delete=models.CASCADE)
    booking_status = models.IntegerField(default=0)
    booking_amount = models.IntegerField(default=0)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    book=models.ForeignKey(tbl_book,on_delete=models.SET_NULL,null=True)
    journal=models.ForeignKey(tbl_journal,on_delete=models.SET_NULL,null=True)
    datetime=models.DateTimeField(auto_now_add=True)