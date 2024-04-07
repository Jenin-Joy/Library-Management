from django.urls import path
from User import views
app_name = "webuser"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),

    path('profile/',views.profile,name="profile"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('change_password/',views.change_password,name="change_password"),

    path('viewbook/',views.viewbook,name="viewbook"),
    path('book_booking/<int:id>',views.book_booking,name="book_booking"),

    path('view_booking/',views.view_booking,name="view_booking"),
    path('payment/<int:id>',views.payment,name="payment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

    path('viewjournal/',views.viewjournal,name="viewjournal"),
    path('journal_booking/<int:id>',views.journal_booking,name="journal_booking"),
    path('journalpayment/<int:id>',views.journalpayment,name="journalpayment"),

    path('complaint/',views.complaint,name="complaint"),
    path('viewdocument/',views.viewdocument,name="viewdocument"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('logout/',views.logout,name="logout"),
]