from django.db import models

class LiniaProdukcyjnaQuerySet(models.QuerySet):     
    def maszyny_ws1(self):
        return self.filter(Nazwa_linii='WS1').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws2a(self):
        return self.filter(Nazwa_linii='WS2a').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws2b(self):
        return self.filter(Nazwa_linii='WS2b').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws3a(self):
        return self.filter(Nazwa_linii='WS3a').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws3b(self):
        return self.filter(Nazwa_linii='WS3b').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws4(self):
        return self.filter(Nazwa_linii='WS4').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws5(self):
        return self.filter(Nazwa_linii='WS5').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws6(self):
        return self.filter(Nazwa_linii='WS6').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws7(self):
        return self.filter(Nazwa_linii='WS7').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws8(self):
        return self.filter(Nazwa_linii='WS8').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws9(self):
        return self.filter(Nazwa_linii='WS9').first().maszyny_linii_produkcyjnej.all()
    def maszyny_ws10(self):
        return self.filter(Nazwa_linii='WS10').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf1(self):
        return self.filter(Nazwa_linii='STF1').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf2(self):
        return self.filter(Nazwa_linii='STF2').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf3(self):
        return self.filter(Nazwa_linii='STF3').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf4(self):
        return self.filter(Nazwa_linii='STF4').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf5(self):
        return self.filter(Nazwa_linii='STF5').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf6(self):
        return self.filter(Nazwa_linii='STF6').first().maszyny_linii_produkcyjnej.all()
    def maszyny_stf7(self):
        return self.filter(Nazwa_linii='STF7').first().maszyny_linii_produkcyjnej.all()
    
class LiniaProdukcyjnaManager(models.Manager):

    def get_queryset(self):
        return LiniaProdukcyjnaQuerySet(self.model, using=self._db)

    def ws1_maszyny(self):
        return self.get_queryset().maszyny_ws1()

    def ws2a_maszyny(self):
        return self.get_queryset().maszyny_ws2a()

    def ws2b_maszyny(self):
        return self.get_queryset().maszyny_ws2b()

    def ws3a_maszyny(self):
        return self.get_queryset().maszyny_ws3a()

    def ws3b_maszyny(self):
        return self.get_queryset().maszyny_ws3b()

    def ws4_maszyny(self):
        return self.get_queryset().maszyny_ws4()

    def ws5_maszyny(self):
        return self.get_queryset().maszyny_ws5()

    def ws6_maszyny(self):
        return self.get_queryset().maszyny_ws6()

    def ws7_maszyny(self):
        return self.get_queryset().maszyny_ws7()

    def ws8_maszyny(self):
        return self.get_queryset().maszyny_ws8()

    def ws9_maszyny(self):
        return self.get_queryset().maszyny_ws9()

    def ws10_maszyny(self):
        return self.get_queryset().maszyny_ws10()

    def stf1_maszyny(self):
        return self.get_queryset().maszyny_stf1()

    def stf2_maszyny(self):
        return self.get_queryset().maszyny_stf2()

    def stf3_maszyny(self):
        return self.get_queryset().maszyny_stf3()

    def stf4_maszyny(self):
        return self.get_queryset().maszyny_stf4()

    def stf5_maszyny(self):
        return self.get_queryset().maszyny_stf5()

    def stf6_maszyny(self):
        return self.get_queryset().maszyny_stf6()

    def stf7_maszyny(self):
        return self.get_queryset().maszyny_stf7()
