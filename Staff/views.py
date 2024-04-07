from django.shortcuts import render,redirect
from Admin.models import *
from Staff.models import *
from User.models import *
from datetime import date
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    return render(request,"Staff/HomePage.html")

def profile(request):
    staff = tbl_staff.objects.get(id=request.session['sid'])
    return render(request,"Staff/Profile.html",{"staff":staff})

def edit_profile(request):
    staff = tbl_staff.objects.get(id=request.session['sid'])
    if request.method == "POST":
        staff.staff_name = request.POST.get("staff_name")
        staff.staff_contact = request.POST.get("staff_contact")
        staff.staff_email = request.POST.get("staff_email")
        staff.staff_address = request.POST.get("staff_address")
        staff.save()
        return redirect("webstaff:profile")
    else:
        return render(request,"Staff/Editprofile.html",{"staff":staff})

def change_password(request):
    staff = tbl_staff.objects.get(id=request.session['sid'])
    if request.method == "POST":
        if staff.staff_password == request.POST.get("staff_oldpassword"):
            if request.POST.get("staff_newpassword") == request.POST.get("staff_repassword"):
                staff.staff_password = request.POST.get("staff_repassword")
                staff.save()
                return render(request,"Staff/Profile.html",{"msg":"profile updated"})
            else:
                return render(request,"Staff/Changepassword.html",{"msg":"Error in Repassword"})
        else:
            return render(request,"Staff/Changepassword.html",{"msg":"Error in Oldpassword"})
    else:
        return render(request,"User/Changepassword.html")

def book(request):
    books = tbl_book.objects.all()
    category = tbl_category.objects.all()
    if request.method == "POST":
        tbl_book.objects.create(book_name=request.POST.get("txt_name"),
            book_author=request.POST.get("txt_auth"),
            book_publisher=request.POST.get("txt_pub"),
            book_description=request.POST.get("txt_desc"),
            book_image=request.FILES.get("txt_photo"),
            book_price=request.POST.get("txt_price"),
            category=tbl_category.objects.get(id=request.POST.get("sel_category")),
            staff=tbl_staff.objects.get(id=request.session['sid']))
        return redirect("webstaff:book")
    else:
        return render(request,"Staff/Add_books.html",{"category":category,"book":books})

def delete_book(request,id):
    tbl_book.objects.get(id=id).delete()
    return redirect("webstaff:book")

def view_book_booking(request):
    bookings = tbl_book_booking.objects.all()
    return render(request,"Staff/View_book_booking.html",{"booking":bookings})

def book_collected(request,id):
    book = tbl_book_booking.objects.get(id=id)
    book.booking_status = 1
    book.collected_date = date.today()
    book.return_date = date.today() + timedelta(days=30)
    book.save()
    bk = tbl_book.objects.get(id=book.book.id)
    bk.book_status = 1
    bk.save()
    # today = timezone.now().date()
    # one_month_later = today + timedelta(days=30)
    # print( date.today() + timedelta(days=30))
    return redirect("webstaff:view_book_booking")

def book_returned(request,id):
    book = tbl_book_booking.objects.get(id=id)
    book.booking_status = 2
    book.returned_date = date.today()
    book.save()
    bk = tbl_book.objects.get(id=book.book.id)
    bk.book_status = 0
    bk.save()
    return redirect("webstaff:view_book_booking")

def book_returned_premium(request,id):
    book = tbl_book_booking.objects.get(id=id)
    book.booking_status = 6
    book.returned_date = date.today()
    book.save()
    bk = tbl_book.objects.get(id=book.book.id)
    bk.book_status = 0
    bk.save()
    return redirect("webstaff:view_book_booking")

def ajaxamount(request):
    book = tbl_book_booking.objects.get(id=request.GET.get("id"))
    book.booking_status = 3
    book.booking_amount = request.GET.get("amt")
    book.save()
    return JsonResponse({"msg":"Amount Updated"})
    
def journal(request):
    journals = tbl_journal.objects.all()
    if request.method == "POST":
        tbl_journal.objects.create(journal_name=request.POST.get("txt_name"),
            journal_volume=request.POST.get("txt_vol"),
            journal_publisher=request.POST.get("txt_pub"),
            journal_topic=request.POST.get("txt_topic"),
            journal_image=request.FILES.get("txt_photo"),
            journal_price=request.POST.get("txt_price"),
            staff=tbl_staff.objects.get(id=request.session['sid']))
        return redirect("webstaff:journal")
    else:
        return render(request,"Staff/Add_journals.html",{"journal":journals})

def delete_journal(request,id):
    tbl_journal.objects.get(id=id).delete()
    return redirect("webstaff:journal")

def view_journal_booking(request):
    bookings = tbl_journal_booking.objects.all()
    return render(request,"Staff/View_journal_booking.html",{"booking":bookings})

def journal_collected(request,id):
    book = tbl_journal_booking.objects.get(id=id)
    book.booking_status = 1
    book.collected_date = date.today()
    book.return_date = date.today() + timedelta(days=30)
    book.save()
    bk = tbl_journal.objects.get(id=book.journal.id)
    bk.journal_status = 1
    bk.save()
    # today = timezone.now().date()
    # one_month_later = today + timedelta(days=30)
    # print( date.today() + timedelta(days=30))
    return redirect("webstaff:view_journal_booking")

def journal_returned(request,id):
    book = tbl_journal_booking.objects.get(id=id)
    book.booking_status = 2
    book.returned_date = date.today()
    book.save()
    bk = tbl_journal.objects.get(id=book.journal.id)
    bk.journal_status = 0
    bk.save()
    return redirect("webstaff:view_journal_booking")

def journal_returned_premium(request,id):
    book = tbl_journal_booking.objects.get(id=id)
    book.booking_status = 6
    book.returned_date = date.today()
    book.save()
    bk = tbl_journal.objects.get(id=book.journal.id)
    bk.journal_status = 0
    bk.save()
    return redirect("webstaff:view_journal_booking")

def ajaxjournalamount(request):
    book = tbl_journal_booking.objects.get(id=request.GET.get("id"))
    book.booking_status = 3
    book.booking_amount = request.GET.get("amt")
    book.save()
    return JsonResponse({"msg":"Amount Updated"})

def lentbooks(request):
    book = tbl_book_booking.objects.filter(booking_status=1)
    booking = tbl_journal_booking.objects.filter(booking_status=1)
    return render(request,"Staff/Lent_Books.html",{"book":book,"booking":booking})

def logout(request):
    del request.session['sid']
    return redirect("webguest:login")