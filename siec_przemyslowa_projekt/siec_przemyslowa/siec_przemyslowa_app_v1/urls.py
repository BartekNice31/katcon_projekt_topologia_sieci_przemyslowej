from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('database_main_page',views.baza_danych_linie_produkcyjne,name='database_main_page')
    ,path('application_main_page/',views.powrot_strona_glowna,name='main_page_application')
    ,path('wyswietl_linie_produkcyjne/',views.wyswietl_linie_produkcyjne,name='wyswietl_linie_produkcyjne')
    ,path('wyswietl_maszyny_linii_produkcyjnej_po_nazwie/<str:nazwa_linia_produkcyjna>',views.wyswietl_maszyny_linii_produkcyjnej_po_nazwie
          ,name='wyswietl_maszyny_linii_produkcyjnej_po_nazwie')
    ,path('wyswietl_maszyny_linii_produkcyjnej_po_id<int:id_linii_produkcyjnej>',views.wyswietl_maszyny_linii_produkcyjnej_po_id
          ,name='wyswietl_maszyny_linii_produkcyjnej_po_id')
]