from django.urls import path
from Staff import views
app_name = "webstaff"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),

    path('profile/',views.profile,name="profile"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('change_password/',views.change_password,name="change_password"),

    path('book/',views.book,name="book"),
    path('delete_book/<int:id>',views.delete_book,name="delete_book"),

    path('view_book_booking/',views.view_book_booking,name="view_book_booking"),
    path('book_collected/<int:id>',views.book_collected,name="book_collected"),
    path('book_returned/<int:id>',views.book_returned,name="book_returned"),
    path('book_returned_premium/<int:id>',views.book_returned_premium,name="book_returned_premium"),
    path('ajaxamount/',views.ajaxamount,name="ajaxamount"),

    path('journal/',views.journal,name="journal"),
    path('delete_journal/<int:id>',views.delete_journal,name="delete_journal"),

    path('view_journal_booking/',views.view_journal_booking,name="view_journal_booking"),
    path('journal_collected/<int:id>',views.journal_collected,name="journal_collected"),
    path('journal_returned/<int:id>',views.journal_returned,name="journal_returned"),
    path('journal_returned_premium/<int:id>',views.journal_returned_premium,name="journal_returned_premium"),
    path('ajaxjournalamount/',views.ajaxjournalamount,name="ajaxjournalamount"),

    path('lentbooks/',views.lentbooks,name="lentbooks"),

    path('logout/',views.logout,name="logout"),

]