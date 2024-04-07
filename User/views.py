from django.shortcuts import render,redirect
from Guest.models import *  
from Staff.models import *  
from User.models import * 
from django.http import JsonResponse 
# Create your views here.

def homepage(request):
    user  = tbl_user.objects.get(id=request.session["uid"])
    usertype = user.types
    return render(request,"User/HomePage.html",{"usertype":usertype})

def profile(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/Profile.html",{"user":user})

def edit_profile(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        user.user_name = request.POST.get("user_name")
        user.user_contact = request.POST.get("user_contact")
        user.user_email = request.POST.get("user_email")
        user.user_address = request.POST.get("user_address")
        user.save()
        return redirect("webuser:profile")
    else:
        return render(request,"User/Editprofile.html",{"user":user})

def change_password(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        if user.user_password == request.POST.get("user_oldpassword"):
            if request.POST.get("user_newpassword") == request.POST.get("user_repassword"):
                user.user_password = request.POST.get("user_repassword")
                user.save()
                return render(request,"User/Profile.html",{"msg":"profile updated"})
            else:
                return render(request,"User/Changepassword.html",{"msg":"Error in Repassword"})
        else:
            return render(request,"User/Changepassword.html",{"msg":"Error in Oldpassword"})
    else:
        return render(request,"User/Changepassword.html")

def viewbook(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    books = tbl_book.objects.filter(book_status=0)
    for i in books:
        tot=0
        ratecount=tbl_rating.objects.filter(book=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(book=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(books,parry)
    return render(request,"User/View_books.html",{"books":datas,"ar":ar})

def book_booking(request,id):
    user  = tbl_user.objects.get(id=request.session["uid"])
    usertype = user.types
    if usertype >= 2:
        tbl_book_booking.objects.create(
            user=tbl_user.objects.get(id=request.session['uid']),
            book=tbl_book.objects.get(id=id),
            booking_status = 5
        )
        bk = tbl_book.objects.get(id=id)
        bk.book_status = 1
        bk.save()
        return render(request,"User/View_books.html",{"msg":"Booked"})
    else:
        duecount = tbl_book_booking.objects.filter(booking_status__lte=3).count()
        if duecount > 0:
            return render(request,"User/View_books.html",{"msg":"Check Your Dues"})
        else:
            tbl_book_booking.objects.create(
                user=tbl_user.objects.get(id=request.session['uid']),
                book=tbl_book.objects.get(id=id),
            )
            return render(request,"User/View_books.html",{"msg":"Booked"})

def view_booking(request):
    bookings = tbl_book_booking.objects.filter(user=request.session['uid'])
    journals = tbl_journal_booking.objects.filter(user=request.session['uid'])
    return render(request,"User/My_booking.html",{"booking":bookings,"journal":journals})

def payment(request,id):
    book = tbl_book_booking.objects.get(id=id)
    if request.method == "POST":
        book.booking_status = 4
        book.save()
        return redirect("webuser:loader")
    else:
        return render(request,"User/Payment.html",{"book":book})
        
def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def viewjournal(request):
    journals = tbl_journal.objects.filter(journal_status=0)
    return render(request,"User/View_journals.html",{"journals":journals})

def journal_booking(request,id):
    user  = tbl_user.objects.get(id=request.session["uid"])
    usertype = user.types
    if usertype >= 2:
        tbl_journal_booking.objects.create(
            user=tbl_user.objects.get(id=request.session['uid']),
            journal=tbl_journal.objects.get(id=id),
            booking_status = 5
        )
        bk = tbl_journal.objects.get(id=id)
        bk.journal_status = 1
        bk.save()
        return render(request,"User/View_journals.html",{"msg":"Booked"})
    else:
        duecount = tbl_journal_booking.objects.filter(booking_status__lte=3).count()
        if duecount> 0:
            return render(request,"User/View_journals.html",{"msg":"Check Your Dues"})
        else:
            tbl_journal_booking.objects.create(
                user=tbl_user.objects.get(id=request.session['uid']),
                journal=tbl_journal.objects.get(id=id),
            )
            return render(request,"User/View_journals.html",{"msg":"Booked"})

def journalpayment(request,id):
    book = tbl_journal_booking.objects.get(id=id)
    if request.method == "POST":
        book.booking_status = 4
        book.save()
        return redirect("webuser:loader")
    else:
        return render(request,"User/Payment.html",{"book":book})

def complaint(request):
    complaint = tbl_complaint.objects.filter(user=request.session['uid'])
    if request.method == "POST":
        tbl_complaint.objects.create(complaint_content=request.POST.get("txt_complaint"),
            user=tbl_user.objects.get(id=request.session['uid']))
        return redirect("webuser:complaint")
    else:
        return render(request,"User/Complaint.html",{"complaint":complaint})

def viewdocument(request):
    doc = tbl_document.objects.all()
    return render(request,"User/View_doument.html",{"document":doc})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_book_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(book=wdata.book_id).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(book=wdata.book_id).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_book_booking.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,book=tbl_book.objects.get(id=wdata.book_id))
    stardata=tbl_rating.objects.filter(book=wdata.book_id).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    cdata = tbl_book_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(book=cdata.book_id)
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + int(i.rating_data)
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)


def logout(request):
    del request.session['uid']
    return redirect("webguest:login")