from django.shortcuts import render,get_object_or_404
from . import models
from .utils import ping
from . import checktcp

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
    return render(request,'urzadzenia_maszyna_produkcyjna.html',{'data':urzadzenia,'nazwa_maszyny_produkcyjnej':nazwa_maszyny_produkcyjnej})

def szczegoly_urzadzenia(request, nazwa_maszyny_produkcyjnej):
    urzadzenie = models.UrzadzenieMaszyny.objects.filter(
        Nazwa_urzadzenia=nazwa_maszyny_produkcyjnej
    ).first()
    # urzadzenie.status=checktcp.check_tcp(ip=urzadzenie.Ip_Adres,port=502,timeout=1)
    urzadzenie.status=ping(urzadzenie.Ip_Adres)
    print(ping(urzadzenie.Ip_Adres))
    print(urzadzenie)
    urzadzenie.save()

    # return render(request, "urzadzenia_maszyna_produkcyjna.html", {
    #     "data": data,
    #     "nazwa_maszyna_produkcyjna": nazwa,
    # })

    urzadzenia=models.UrzadzenieMaszyny.objects.all()
    return render(request,'urzadzenia_maszyna_produkcyjna.html',{'data':urzadzenia,'nazwa_maszyny_produkcyjnej':nazwa_maszyny_produkcyjnej,'urzadzenie':urzadzenie})