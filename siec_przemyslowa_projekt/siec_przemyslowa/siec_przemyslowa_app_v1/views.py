from django.shortcuts import render
from . import models

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
    return render(request,'maszyny_linia_produkcyjna.html',{'data':maszyny})

def wyswietl_maszyny_linii_produkcyjnej_po_id(request,id_linii_produkcyjnej):
    linia_produkcyjna=models.LiniaProdukcyjna.objects.filter(id=id_linii_produkcyjnej).first()
    maszyny=linia_produkcyjna.maszyny_linii_produkcyjnej.all()
    return render(request,'maszyny_linia_produkcyjna.html',{'data':maszyny})