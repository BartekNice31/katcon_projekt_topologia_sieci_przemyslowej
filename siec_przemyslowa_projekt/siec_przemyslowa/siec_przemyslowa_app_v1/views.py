from django.shortcuts import render,get_object_or_404,redirect
from . import models
from .utils import  is_device_online,arp_ping
from . import checktcp
from . import forms
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from django.core.cache import cache
import time

def get_device_status(ip):
    key = f"device_status_{ip}"
    cached = cache.get(key)

    if cached is not None:
        return cached

    status = is_device_online(ip)
    cache.set(key, status, timeout=60)  # 60 sekund
    return status

# Create your views here.
def baza_danych_linie_produkcyjne(request):
    return render(request,'database_main_page.html')

def powrot_strona_glowna(request):
    return render(request,'homepage.html')

def wyswietl_linie_produkcyjne(request):
    linie_produkcyjne=models.LiniaProdukcyjna.objects.all()

    return render(request,'linie_produkcyjne_lista.html',{'data':linie_produkcyjne})

def wyswietl_maszyny_linii_produkcyjnej_po_nazwie(request,nazwa_linia_produkcyjna):
    linia_produkcyjna=models.LiniaProdukcyjna.objects.filter(Nazwa_linii=nazwa_linia_produkcyjna).first()
    maszyny=linia_produkcyjna.maszyny_linii_produkcyjnej.all()
    return render(request,'maszyny_linia_produkcyjna.html',{'data':maszyny,'linia_produkcyjna':nazwa_linia_produkcyjna}) 

def wyswietl_urzadzenia_maszyny_produkcyjnej_po_nazwie(request,nazwa_maszyny_produkcyjnej):
    maszyna_produkcyjna=models.MaszynaProdukcyjna.objects.filter(Maszyna_nazwa=nazwa_maszyny_produkcyjnej).first()
    urzadzenia=maszyna_produkcyjna.urzadzenia_maszyny_produkcyjnej.all()

    for urzadzenie in urzadzenia:
        # urzadzenie.Status_Polaczenia=is_device_online(urzadzenie.Ip_Adres)
        urzadzenie.Status_Polaczenia = get_device_status(urzadzenie.Ip_Adres)
        # print(arp_ping(urzadzenie.Ip_Adres)["online"])
        # print(arp_ping(urzadzenie.Ip_Adres)["ip"])
        # print(arp_ping(urzadzenie.Ip_Adres)["mac"])
        # urzadzenie.Status_Polaczenia=arp_ping(urzadzenie.Ip_Adres)["online"]
        urzadzenie.save()

    return render(request,'urzadzenia_maszyna_produkcyjna.html',{'data':urzadzenia,'nazwa_maszyny_produkcyjnej':nazwa_maszyny_produkcyjnej})

# def szczegoly_urzadzenia(request, nazwa_maszyny_produkcyjnej):
#     urzadzenie = models.UrzadzenieMaszyny.objects.filter(
#         Nazwa_urzadzenia=nazwa_maszyny_produkcyjnej
#     ).first()
#     # urzadzenie.status=checktcp.check_tcp(ip=urzadzenie.Ip_Adres,port=502,timeout=1)
#     urzadzenie.status=ping(urzadzenie.Ip_Adres)
#     print(ping(urzadzenie.Ip_Adres))
#     print(urzadzenie)
#     urzadzenie.save()

#     # return render(request, "urzadzenia_maszyna_produkcyjna.html", {
#     #     "data": data,
#     #     "nazwa_maszyna_produkcyjna": nazwa,
#     # })

#     urzadzenia=models.UrzadzenieMaszyny.objects.all()
#     return render(request,'urzadzenia_maszyna_produkcyjna.html',{'data':urzadzenia,'nazwa_maszyny_produkcyjnej':nazwa_maszyny_produkcyjnej,'urzadzenie':urzadzenie})

def dodaj_linie_produkcyjna(request):
    if request.method=="POST":
        form=forms.LiniaProdukcyjnaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("wyswietl_linie_produkcyjne")
    else:
        form=forms.LiniaProdukcyjnaForm()
    return render(request,"dodaj_linie_produkcyjna.html",{"form":form})

def dodaj_maszyne_produkcyjna(request):
    if request.method=="POST":
        form=forms.MaszynaProdukcyjnaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("wyswietl_linie_produkcyjne")
    else:
        form=forms.MaszynaProdukcyjnaForm()
    return render(request,"dodaj_maszyne_produkcyjna.html",{"form":form})

def dodaj_urzadzenie_maszyny_produkcyjnej(request):
    if request.method=="POST":
        form=forms.UrzadzenieMaszynyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("wyswietl_linie_produkcyjne")
    else:
        form=forms.UrzadzenieMaszynyForm()
    return render(request,"dodaj_urzadzenie_maszyny_produkcyjnej.html",{"form":form})

def dodaj_do_bazy_danych_strona(request):
    return render(request,'dodawanie_do_bazy_danych.html')

def edytuj_linie_produkcyjna(request,id):
    linia_produkcyjna_do_edycji=get_object_or_404(models.LiniaProdukcyjna,id=id)
    if request.method=="POST":
        form=forms.LiniaProdukcyjnaForm(request.POST,instance=linia_produkcyjna_do_edycji)
        if form.is_valid():
            form.save()
            return redirect('wyswietl_linie_produkcyjne')
    else:
        form=forms.LiniaProdukcyjnaForm(instance=linia_produkcyjna_do_edycji)
    return render(
        request
        ,'edytuj_linie_produkcyjna_form.html'
        ,{'form':form}
    )

def usun_linie_produkcyjna(request,id):
    # linia_produkcyjna_do_usuniecia=get_object_or_404(models.LiniaProdukcyjna)
    linia_produkcyjna_do_usuniecia=models.LiniaProdukcyjna.objects.get(id=id)
    linia_produkcyjna_do_usuniecia.delete()
    return redirect('wyswietl_linie_produkcyjne')

def edytuj_maszyne_produkcyjna(request,id):
    maszyna_produkcyjna_do_edycji=models.MaszynaProdukcyjna.objects.get(id=id)
    if request.method=="POST":
        form=forms.MaszynaProdukcyjnaForm(request.POST,instance=maszyna_produkcyjna_do_edycji)
        if form.is_valid():
            form.save()
            return redirect('wyswietl_linie_produkcyjne')
    else:
        form=forms.MaszynaProdukcyjnaForm(instance=maszyna_produkcyjna_do_edycji)
    return render(
        request
        ,'edytuj_maszyne_produkcyjna.html'
        ,{'form':form}
    )

def usun_maszyne_produkcyjna(request,id):
    maszyna_produkcyjna_do_usuniecia=models.MaszynaProdukcyjna.objects.get(id=id)
    maszyna_produkcyjna_do_usuniecia.delete()
    return redirect('wyswietl_linie_produkcyjne')

def edytuj_urzadzenie_maszyny_produkcyjnej(request,id):
    urzadzenie_maszyny_produkcyjnej_do_edycji=models.UrzadzenieMaszyny.objects.get(id=id)
    if request.method=="POST":
        form=forms.UrzadzenieMaszynyForm(request.POST,instance=urzadzenie_maszyny_produkcyjnej_do_edycji)
        if form.is_valid():
            form.save()
            return redirect('wyswietl_linie_produkcyjne')
    else:
        form=forms.UrzadzenieMaszynyForm(instance=urzadzenie_maszyny_produkcyjnej_do_edycji)
    return render(
        request
        ,'edytuj_urzadzenie_maszyny_produkcyjnej.html'
        ,{'form':form}
    )

def usun_urzadzenie_maszyny_produkcyjnej(request,id):
    urzadzenie_maszyny_produkcyjnej_do_usuniecia=models.UrzadzenieMaszyny.objects.get(id=id)
    urzadzenie_maszyny_produkcyjnej_do_usuniecia.delete()
    return render(request,'wyswietl_linie_produkcyjne')

