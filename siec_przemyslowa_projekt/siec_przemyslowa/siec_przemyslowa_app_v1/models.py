from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator
from . modele.models_devices import *
from . modele.models_line_productions import *
from . modele.modele_status_urzadzenia import *
from . managers.managers_linia_produkcyjna import *
from . managers.managers_urzadzenia_maszyny import *
from datetime import datetime
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
class LiniaProdukcyjna(models.Model):
    Nazwa_linii=models.CharField(max_length=255,unique=True,blank=False,null=False)
    Strefa_linia_produkcyjna=models.IntegerField(choices=LiniaProdukcyjnaStrefa.choices,unique=False,blank=False,null=False)
    Opis=models.CharField(null=False,blank=True,max_length=1000,default='')

    objects=models.Manager()
    linie_produkcyjne=LiniaProdukcyjnaManager()
    def __str__(self):
        return f"Linia produkcyjna: {self.Nazwa_linii} {self.Strefa_linia_produkcyjna}"

    class Meta:
        verbose_name='Lina Produkcyjna'
        verbose_name_plural='Linie produkcyjne'
        ordering=['Nazwa_linii']

# @receiver([pre_save],sender=LiniaProdukcyjna)
# def zapisz_linie_produkcyjna_przed(sender,instance,**kwargs):
#     print("Właśnie mamy zapisać: ")
#     nasza_linia_produkcyjna=LiniaProdukcyjna.objects.get(id=instance.id)
#     print(f"{nasza_linia_produkcyjna.Nazwa_linii}")

@receiver([post_save],sender=LiniaProdukcyjna)
def zapisz_linie_produkcyjna_przed(sender,instance,**kwargs):
    print("Właśnie zapisaliśmy: ") 
    print(f"{instance.Nazwa_linii}")
class MaszynaProdukcyjna(models.Model):
    Maszyna_nazwa=models.CharField(unique=False,blank=False,
                                   max_length=255,
                                   validators=[MinLengthValidator(10)])
    Linia_produkcyjna=models.ForeignKey(LiniaProdukcyjna
                                    ,on_delete=models.CASCADE
                                    ,related_name="maszyny_linii_produkcyjnej"
                                    ,blank=False,null=False)
    Opis=models.CharField(null=False,blank=True,max_length=1000,default='')

    # objects=models.Manager()


    def __str__(self):
        return f'Maszyna produkcyjna: {self.Maszyna_nazwa} {self.Linia_produkcyjna}' 
    
    class Meta:
        verbose_name='Maszyna produkcyjna'
        verbose_name_plural='Maszyny produkcyjne'
        ordering=['Maszyna_nazwa']

# @receiver([pre_save],sender=MaszynaProdukcyjna)
# def zapisz_maszyne_produkcyjna_przed(sender,instance,**kwargs):
#     print("Właśnie mamy zapisać maszynę produkcyjną:")
#     nasza_maszyna_produkcyjna=MaszynaProdukcyjna.objects.get(id=instance.id)
#     print(f"{nasza_maszyna_produkcyjna.Maszyna_nazwa}")

@receiver([post_save],sender=MaszynaProdukcyjna)
def zapisz_maszyne_produkcyjna_po(sender,instance,**kwargs):
    print("Właśnie zapisaliśmy maszynę produkcyjną:")
    print(f"{instance.Maszyna_nazwa}")
class UrzadzenieMaszyny(models.Model):
    Nazwa_urzadzenia=models.CharField(unique=False,blank=False,null=False
                                      ,max_length=255
                                      ,validators=[
                                          MinLengthValidator(10)
                                      ])
    Ip_Adres=models.CharField(unique=True,null=False,blank=False
                            ,max_length=17
                            ,validators=[
                                MinLengthValidator(7)
                            ])
    Rodzaj_Urzadzenia=models.IntegerField(choices=TypUrzadzenia.choices,null=False,blank=False,unique=False
                                          ,max_length=255)
    Maszyna_produkcyjna=models.ForeignKey(MaszynaProdukcyjna,on_delete=models.CASCADE,null=False
                                        ,unique=False,blank=False,related_name="urzadzenia_maszyny_produkcyjnej")
    Opis=models.CharField(null=False,blank=True,max_length=1000,default='')

    Status_Polaczenia=models.IntegerField(choices=StatusPolaczenia.choices,null=False,blank=True,default=StatusPolaczenia.OFFLINE)


    def __str__(self):
        return f"Urzadzenie maszyny: {self.Nazwa_urzadzenia} {self.Ip_Adres} {self.Rodzaj_Urzadzenia}"

    class Meta:
        verbose_name='Urządzenie w maszynie'
        verbose_name_plural='Urządzenia w maszynie'
        ordering=['Ip_Adres']

# @receiver([pre_save],sender=UrzadzenieMaszyny)
# def zapisz_urzadzenie_maszyny_produkcyjnej_przed(sender,instance,**kwargs):
#     print("Właśnie mamy zapisać urządzenie maszyny produkcyjnej:")
#     nasze_urzadzenie_maszyny=UrzadzenieMaszyny.objects.get(id=instance.id)
#     print(f"{nasze_urzadzenie_maszyny.Nazwa_urzadzenia}")

@receiver([post_save],sender=UrzadzenieMaszyny)
def zapisz_urzadzenie_maszyny_produkcyjnej_po(sender,instance,**kwargs):
    print("Właśnie zapisaliśmy urządzenie maszyny produkcyjnej:")
    print(f"{instance.Nazwa_urzadzenia}")