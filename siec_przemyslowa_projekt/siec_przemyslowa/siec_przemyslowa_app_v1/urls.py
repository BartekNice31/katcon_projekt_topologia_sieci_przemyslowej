from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('database_main_page',views.baza_danych_linie_produkcyjne,name='database_main_page')
    ,path('application_main_page/',views.powrot_strona_glowna,name='main_page_application')
    ,path('wyswietl_linie_produkcyjne/',views.wyswietl_linie_produkcyjne,name='wyswietl_linie_produkcyjne')
    ,path('wyswietl_maszyny_linii_produkcyjnej_po_nazwie/<str:nazwa_linia_produkcyjna>',views.wyswietl_maszyny_linii_produkcyjnej_po_nazwie
          ,name='wyswietl_maszyny_linii_produkcyjnej_po_nazwie')
      ,path('wyswietl_urzadzenia_maszyny_produkcyjnej/<str:nazwa_maszyny_produkcyjnej>',views.wyswietl_urzadzenia_maszyny_produkcyjnej_po_nazwie,
            name='wyswietl_urzadzenia_maszyny_produkcyjnej')
    # ,path('szczegoly_urzadzenia/<str:nazwa_maszyny_produkcyjnej>',views.szczegoly_urzadzenia,name='szczegoly_urzadzenia')
    ,path('dodaj_linie_produkcyjna_formularz',views.dodaj_linie_produkcyjna,name="dodaj_linie_produkcyjna_formularz")
    ,path('dodaj_maszyne_produkcyjna_formularz',views.dodaj_maszyne_produkcyjna,name="dodaj_maszyne_produkcyjna_formularz")
    ,path('dodaj_urzadzenie_maszyny_produkcyjnej_formularz',views.dodaj_urzadzenie_maszyny_produkcyjnej
          ,name='dodaj_urzadzenie_maszyny_produkcyjnej_formularz')
    ,path('dodaj_do_bazy_danych_strona',views.dodaj_do_bazy_danych_strona,name='dodaj_do_bazy_danych_strona')
]