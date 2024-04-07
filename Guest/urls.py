from django.urls import path
from Guest import views
app_name = "webguest"
urlpatterns = [
    path('user_reg/',views.user_reg,name="user_reg"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('login/',views.login,name="login"),

    path('payment/',views.payment,name="payment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

    path('',views.index,name="index"),
]