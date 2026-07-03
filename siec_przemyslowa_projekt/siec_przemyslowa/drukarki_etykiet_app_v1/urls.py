from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('printers_home_page',views.printers_home_page,name='printers_home_page')
    ,path('database_printers_page',views.database_printers_page,name='database_printers_page')
    ,path('add_new_printer',views.add_new_printer,name='add_new_printer')
    ,path('edit_printer/<int:id>',views.edit_printer,name='edit_printer')
    ,path('remove_printer/<int:id>',views.remove_printer,name='remove_printer')
]