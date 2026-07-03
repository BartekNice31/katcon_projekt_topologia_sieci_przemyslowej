from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('printers_home_page',views.printers_home_page,name='printers_home_page')
    ,path('database_printers_page',views.database_printers_page,name='database_printers_page')
]