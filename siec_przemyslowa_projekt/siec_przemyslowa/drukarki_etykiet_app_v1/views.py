from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from . import utils
# Create your views here.

def printers_home_page(request):
    return render(request,'printers_home_page.html')

def database_printers_page(request):
    return render(request,'database_printers.html')