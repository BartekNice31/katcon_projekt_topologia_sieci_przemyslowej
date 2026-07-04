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

# def aktualizuj_github(request): 
#     #C:\Users\bNicewicz\Desktop\projekty\projekty_python\django_siec_przemyslowa\github_send.bat
#     print(GITHUB_FILE)
#     subprocess.run(["cmd.exe", "/c", str(GITHUB_FILE)], text=True)
#     message='MIGRACJA DO SERWERA GITHUB ZAKOŃCZONA.'
#     return render(request,'data_migrations.html',{'message_github':message})

def aktualizuj_github(request):
    bat_file = pathlib.Path(r"C:\Users\bNicewicz\Desktop\projekty\projekty_python\django_siec_przemyslowa\github_send.bat")

    repo_dir = pathlib.Path(r"C:\Users\bNicewicz\Desktop\projekty\projekty_python\django_siec_przemyslowa")

    result = subprocess.run(
        ["cmd.exe", "/c", str(bat_file)],
        cwd=str(repo_dir),   # 🔥 KLUCZOWE
        capture_output=True,
        text=True,
        encoding="utf-8",   # 🔥 KLUCZOWE
        errors="replace"    # 🔥 zabezpieczenie
    )

    print(result.stdout)
    print(result.stderr)

    return render(request, "data_migrations.html", {
        "message_github": result.stdout,
        "message_error": result.stderr
    })