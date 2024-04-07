from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"Admin/HomePage.html")

def admin_registration(request):
    if request.method == "POST":
        tbl_admin.objects.create(admin_name=request.POST.get("txt_name"),admin_contact=request.POST.get("txt_contact"),admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
        return redirect("webadmin:admin_registration")
    else:
        return render(request,"Admin/Admin_Registration.html")

def category(request):
    cat = tbl_category.objects.all()
    if request.method == "POST":
        tbl_category.objects.create(category_name=request.POST.get("txt_name"))
        return redirect("webadmin:category")
    else:
        return render(request,"Admin/Category.html",{"category":cat})

def delete_category(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("webadmin:category")

def edit_category(request,id):
    cat = tbl_category.objects.get(id=id)
    if request.method == "POST":
        cat.category_name = request.POST.get("txt_name")
        cat.save()
        return redirect("webadmin:category")
    else:
        return render(request,"Admin/Category.html",{"cat":cat})

def district(request):
    cat = tbl_district.objects.all()
    if request.method == "POST":
        tbl_district.objects.create(district_name=request.POST.get("txt_name"))
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{"district":cat})

def delete_district(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("webadmin:district")

def edit_district(request,id):
    cat = tbl_district.objects.get(id=id)
    if request.method == "POST":
        cat.district_name = request.POST.get("txt_name")
        cat.save()
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{"cat":cat})

def place(request):
    district = tbl_district.objects.all()
    cat = tbl_place.objects.all()
    if request.method == "POST":
        tbl_place.objects.create(place_name=request.POST.get("txt_name"),district=tbl_district.objects.get(id=request.POST.get("sel_district")))
        return redirect("webadmin:place")
    else:
        return render(request,"Admin/Place.html",{"place":cat,"district":district})

def delete_place(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("webadmin:place")

def edit_place(request,id):
    district = tbl_district.objects.all()
    cat = tbl_place.objects.get(id=id)
    if request.method == "POST":
        cat.place_name = request.POST.get("txt_name")
        cat.district = tbl_district.objects.get(id=request.POST.get("sel_district"))
        cat.save()
        return redirect("webadmin:place")
    else:
        return render(request,"Admin/Place.html",{"cat":cat,"district":district})

# def types(request):
#     types = tbl_type.objects.all()
#     if request.method == "POST":
#         tbl_type.objects.create(type_name=request.POST.get("txt_name"))
#         return redirect("webadmin:types")
#     else:
#         return render(request,"Admin/Type.html",{"type":types})

# def delete_type(request,id):
#     tbl_type.objects.get(id=id).delete()
#     return redirect("webadmin:types")

# def edit_type(request,id):
#     typ = tbl_type.objects.get(id=id)
#     if request.method == "POST":
#         typ.type_name = request.POST.get("txt_name")
#         typ.save()
#         return redirect("webadmin:types")
#     else:
#         return render(request,"Admin/Type.html",{"typ":typ})

def staff(request):
    staff = tbl_staff.objects.all()
    if request.method == "POST":
        tbl_staff.objects.create(staff_name=request.POST.get("txt_name"),staff_contact=request.POST.get("txt_contact"),staff_email=request.POST.get("txt_email"),staff_address=request.POST.get("txt_address"),staff_photo=request.FILES.get("txt_photo"),staff_password=request.POST.get("txt_password"))
        return redirect("webadmin:staff")
    else:
        return render(request,"Admin/Staff.html",{"staff":staff})

def delete_staff(request,id):
    tbl_staff.objects.get(id=id).delete()
    return redirect("webadmin:staff")

def viewcomplaint(request):
    complaint = tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"Admin/View_complaint.html",{"complaint":complaint})

def reply(request,id):
    if request.method == "POST":
        com = tbl_complaint.objects.get(id=id)
        com.complaint_status = 1
        com.complaint_reply = request.POST.get("txt_reply")
        com.save()
        return redirect("webadmin:viewcomplaint")
    else:
        return render(request,"Admin/Reply.html")

def view_replyed_complaint(request):
    complaint = tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/Replyed_complaint.html",{"complaint":complaint})

def viewuser(request):
    user = tbl_user.objects.all()
    return render(request,"Admin/View_user.html",{"user":user})

def add_document(request):
    doc = tbl_document.objects.all()
    if request.method == "POST":
        tbl_document.objects.create(document_name=request.POST.get("txt_name"),
            document_description=request.POST.get("txt_desc"),
            document_image=request.FILES.get("txt_image"))
        return redirect("webadmin:add_document")
    else:
        return render(request,"Admin/Add_document.html",{"document":doc})

def delete_document(request,id):
    tbl_document.objects.get(id=id).delete()
    return redirect("webadmin:add_document")

def accept_user(request,id):
    us = tbl_user.objects.get(id=id)
    us.user_status = 2
    us.save()
    return redirect("webadmin:viewuser")

def reject_user(request,id):
    us = tbl_user.objects.get(id=id)
    us.user_status = 3
    us.save()
    return redirect("webadmin:viewuser")

def report(request):
    book = tbl_book_booking.objects.filter(booking_status=4)
    total = 0
    for b in book:
        total = total + int(b.booking_amount)
    booking = tbl_journal_booking.objects.filter(booking_status=4)
    tot = 0
    for bk in booking:
        tot = tot + int(bk.booking_amount)
    return render(request,"Admin/Report.html",{"book":book,"booking":booking,"bamount":total,"jamount":tot})

def ajaxreport(request):
    if ((request.GET.get("fdate")!="") & (request.GET.get("tdate")!="")):
        book = tbl_book_booking.objects.filter(collected_date__gt=request.GET.get("fdate"),collected_date__lt=request.GET.get("tdate"),booking_status=4)
        total = 0
        for b in book:
            total = total + int(b.booking_amount)
        booking = tbl_journal_booking.objects.filter(collected_date__gt=request.GET.get("fdate"),collected_date__lt=request.GET.get("tdate"),booking_status=4)
        tot = 0
        for bk in booking:
            tot = tot + int(bk.booking_amount)
        return render(request,"Admin/AjaxReport.html",{"book":book,"booking":booking,"bamount":total,"jamount":tot})
    elif request.GET.get("fdate")!="":
        book = tbl_book_booking.objects.filter(collected_date__gt=request.GET.get("fdate"),booking_status=4)
        total = 0
        for b in book:
            total = total + int(b.booking_amount)
        booking = tbl_journal_booking.objects.filter(collected_date__gt=request.GET.get("fdate"),booking_status=4)
        tot = 0
        for bk in booking:
            tot = tot + int(bk.booking_amount)
        return render(request,"Admin/AjaxReport.html",{"book":book,"booking":booking,"bamount":total,"jamount":tot})
    elif request.GET.get("tdate")!="":
        book = tbl_book_booking.objects.filter(collected_date__lt=request.GET.get("tdate"),booking_status=4)
        total = 0
        for b in book:
            total = total + int(b.booking_amount)
        booking = tbl_journal_booking.objects.filter(collected_date__lt=request.GET.get("tdate"),booking_status=4)
        tot = 0
        for bk in booking:
            tot = tot + int(bk.booking_amount)
        return render(request,"Admin/AjaxReport.html",{"book":book,"booking":booking,"bamount":total,"jamount":tot})

def logout(request):
    del request.session['aid']
    return redirect("webguest:login")