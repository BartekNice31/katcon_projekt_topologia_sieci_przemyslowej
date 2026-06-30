from django.db import models

class LiniaProdukcyjnaStrefa(models.IntegerChoices):
    WS1=1,'WS1'
    WS2_A=2,'WS2a'
    WS2_B=3,'WS2b'
    WS3_A=4,'WS3a'
    WS3_B=5,'WS3b'
    WS4=6,'WS4'
    WS5=7,'WS5'
    WS6=8,'WS6'
    WS7=9,'WS7'
    WS8=10,'WS8'
    WS9=11,'WS9'
    WS10=12,'WS10'
    #Linie wciskania- STF

    STF1=20,'STF1'
    STF2=21,'STF2'
    STF3=22,'STF3'
    STF4=23,'STF4'
    STF5=24,'STF5'
    STF6=25,'STF6'
    STF7=26,'STF7'