from django.urls import path
from Admin import views
app_name = "webadmin"
urlpatterns = [
        path('homepage/',views.homepage,name="homepage"),

        path('admin_registration/',views.admin_registration,name="admin_registration"),
        path('category/',views.category,name="category"),
        path('delete_category/<int:id>',views.delete_category,name="delete_category"),
        path('edit_category/<int:id>',views.edit_category,name="edit_category"),

        path('district/',views.district,name="district"),
        path('delete_district/<int:id>',views.delete_district,name="delete_district"),
        path('edit_district/<int:id>',views.edit_district,name="edit_district"),

        path('place/',views.place,name="place"),
        path('delete_place/<int:id>',views.delete_place,name="delete_place"),
        path('edit_place/<int:id>',views.edit_place,name="edit_place"),

        # path('types/',views.types,name="types"),
        # path('delete_type/<int:id>',views.delete_type,name="delete_type"),
        # path('edit_type/<int:id>',views.edit_type,name="edit_type"),

        path('staff/',views.staff,name="staff"),
        path('delete_staff/<int:id>',views.delete_staff,name="delete_staff"),

        path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
        path('reply/<int:id>',views.reply,name="reply"),
        path('view_replyed_complaint/',views.view_replyed_complaint,name="view_replyed_complaint"),

        path('viewuser/',views.viewuser,name="viewuser"),
        path('add_document/',views.add_document,name="add_document"),
        path('delete_document/<int:id>',views.delete_document,name="delete_document"),

        path('accept_user/<int:id>',views.accept_user,name="accept_user"),
        path('reject_user/<int:id>',views.reject_user,name="reject_user"),

        path('report/',views.report,name="report"),
        path('ajaxreport/',views.ajaxreport,name="ajaxreport"),
        

        path('logout/',views.logout,name="logout"),
]