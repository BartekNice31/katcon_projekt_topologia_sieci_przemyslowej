from django.shortcuts import render,redirect
import subprocess
import pathlib

# Create your views here.
BASE_DIR=pathlib.Path(__file__).resolve().parent.parent.parent.parent
GITHUB_FILE=BASE_DIR/'github_send.bat'

def home(request): 
    # print(GITHUB_FILE) 
    # print(pathlib.Path.exists(GITHUB_FILE))
    return render(request,'homepage.html')

def database_main(request):
    return render(request,'siec_przemyslowa_app_v1/database_main_page.html')

def informacje_o_aplikacji(request):
    return render(request,'informations.html')

def migracja_danych(request):
    return render(request,'data_migrations.html')

def aktualizuj_github(request): 
    subprocess.run(["cmd.exe", "/c", str(GITHUB_FILE)], text=True)
    return render(request,'data_migrations.html')