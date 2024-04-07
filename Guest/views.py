from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def index(request):
    return render(request,"Guest/index.html")

def user_reg(request):
    district = tbl_district.objects.all()
    if request.method == "POST":
        if request.POST.get("sel_type") == "3":
            tbl_user.objects.create(user_name = request.POST['txt_name'],
            user_contact = request.POST['txt_contact'],
            user_email = request.POST['txt_email'],
            user_address = request.POST['txt_address'],
            user_photo = request.FILES['txt_photo'],
            types = request.POST.get("sel_type"),
            user_status = 1,
            user_password = request.POST.get('txt_password'),
            place = tbl_place.objects.get(id=request.POST['sel_place']))
            return redirect("webguest:login")
        elif request.POST.get("sel_type") == "2":
            tbl_user.objects.create(user_name = request.POST['txt_name'],
            user_contact = request.POST['txt_contact'],
            user_email = request.POST['txt_email'],
            user_address = request.POST['txt_address'],
            user_photo = request.FILES['txt_photo'],
            types = request.POST.get("sel_type"),
            user_status = 1,
            user_password = request.POST.get('txt_password'),
            place = tbl_place.objects.get(id=request.POST['sel_place']))
            return redirect("webguest:login")
        else:
            tbl_user.objects.create(user_name = request.POST['txt_name'],
            user_contact = request.POST['txt_contact'],
            user_email = request.POST['txt_email'],
            user_address = request.POST['txt_address'],
            user_photo = request.FILES['txt_photo'],
            types = request.POST.get("sel_type"),
            user_password = request.POST.get('txt_password'),
            place = tbl_place.objects.get(id=request.POST['sel_place']))
            request.session["email"] = request.POST['txt_email']
            request.session["password"] = request.POST['txt_password']
            return redirect("webguest:payment")
    else:
        return render(request,"Guest/User_Registration.html",{"district":district})

def ajaxplace(request):
    districtdata=tbl_district.objects.get(id=request.GET.get('did'))
    placedata=tbl_place.objects.filter(district=districtdata)
    return render(request,"Guest/Ajaxplace.html",{'data':placedata})

def login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST['txt_email'],user_password=request.POST['txt_password']).count()
        staffcount = tbl_staff.objects.filter(staff_email=request.POST['txt_email'],staff_password=request.POST['txt_password']).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST['txt_email'],admin_password=request.POST['txt_password']).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST['txt_email'],user_password=request.POST['txt_password'])
            if (user.types == 1) & (user.user_status == 0):
                request.session['uid'] = user.id
                request.session["email"] = user.user_email
                request.session["password"] = user.user_password
                return redirect("webguest:payment")
            elif (user.types == 3) & (user.user_status == 3):
                return render(request,"Guest/Login.html",{'msg':'Request Rejected'})
            elif (user.types == 3) & (user.user_status == 1):
                return render(request,"Guest/Login.html",{'msg':'Request Pending'})
            elif (user.types == 2) & (user.user_status == 3):
                return render(request,"Guest/Login.html",{'msg':'Request Rejected'})
            elif (user.types == 2) & (user.user_status == 1):
                return render(request,"Guest/Login.html",{'msg':'Request Pending'})
            else:
                request.session['uid'] = user.id
                return redirect("webuser:homepage")            
        elif staffcount > 0:
            staff = tbl_staff.objects.get(staff_email=request.POST['txt_email'],staff_password=request.POST['txt_password'])
            request.session['sid'] = staff.id
            return redirect("webstaff:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST['txt_email'],admin_password=request.POST['txt_password'])
            request.session['aid'] = admin.id
            return redirect("webadmin:homepage")
        else:
            return render(request,"Guest/Login.html",{'msg':'Invalid Email or Password'})
    else:
        return render(request,"Guest/Login.html")

def payment(request):
    if (request.session["email"] != "") & (request.session["password"] != ""):
        user = tbl_user.objects.get(user_email=request.session["email"],user_password=request.session["password"])
    elif request.session["uid"] != "":
        user = tbl_user.objects.get(id=request.session["uid"])
    if request.method == "POST":
        user.user_status = 2
        user.save()
        return redirect("webuser:loader")
    else:
        return render(request,"Guest/Payment.html",{"total":"1200"})
        
def loader(request):
    return render(request,"Guest/Loader.html")

def paymentsuc(request):
    return render(request,"Guest/Payment_suc.html")