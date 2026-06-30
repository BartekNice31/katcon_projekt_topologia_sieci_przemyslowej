from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'homepage.html')

def database_main(request):
    return render(request,'siec_przemyslowa_app_v1/database_main_page.html')

def informacje_o_aplikacji(request):
    return render(request,'informations.html')