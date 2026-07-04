from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

from django.db import models


class TypePrinter(models.TextChoices):
    ZD220D = "ZD220D", "Zebra ZD220d"
    ZD220T = "ZD220T", "Zebra ZD220t"
    ZD230D = "ZD230D", "Zebra ZD230d"
    ZD230T = "ZD230T", "Zebra ZD230t"
    ZD411 = "ZD411", "Zebra ZD411"
    ZD421 = "ZD421", "Zebra ZD421"
    ZD611 = "ZD611", "Zebra ZD611"
    ZD621 = "ZD621", "Zebra ZD621"

    GK420D = "GK420D", "Zebra GK420d"
    GK420T = "GK420T", "Zebra GK420t"
    GX420D = "GX420D", "Zebra GX420d"
    GX420T = "GX420T", "Zebra GX420t"
    GX430T = "GX430T", "Zebra GX430t"

    ZT220 = "ZT220", "Zebra ZT220"
    ZT230 = "ZT230", "Zebra ZT230"
    ZT231 = "ZT231", "Zebra ZT231"
    ZT410 = "ZT410", "Zebra ZT410"
    ZT411 = "ZT411", "Zebra ZT411"
    ZT420 = "ZT420", "Zebra ZT420"
    ZT421 = "ZT421", "Zebra ZT421"
    ZT510 = "ZT510", "Zebra ZT510"
    ZT610 = "ZT610", "Zebra ZT610"
    ZT620 = "ZT620", "Zebra ZT620"

    ZM400 = "ZM400", "Zebra ZM400"
    S4M = "S4M", "Zebra S4M"
    SL105_PLUS = "105SLPLUS", "Zebra 105SL Plus"

    OTHER = "OTHER", "Inny model"
class TypeCode(models.TextChoices):
    DATAMATRIX='DATAMATRIX','datamatrix'
    QR="QR","qr"
    PDF_417="PDF_417","pdf_417"
    MERCEDES="MERCEDES","Mercedes"
    DWG_FIAT="DWG_FIAT","dwg_fiat"
    INC_DATA_MATRIX="INC_DATA_MATRIX"
    CNH1="CNH1","cnh1"
    CNH2="CNH2","cnh2"
    QR_TEXT="QR_TEXT","qr_text"
    QR1="QR1","qr1"
    QR2="QR2","qr2"
    DATAMATRIX_PLUS_TITLE="DATAMATRIX_PLUS_TITLE","datamatrix_plus_title"
    UNKNOWN="UNKNOWN","unknown"

class Printer(models.Model):
    name=models.CharField(max_length=100
                        ,null=False
                        ,blank=False
                        ,validators=[
                            MinLengthValidator(10)
                        ])
    ip=models.CharField(max_length=17
                    ,null=False
                    ,blank=False
                    ,unique=True
                    ,validators=[
                        MinLengthValidator(7)
                    ])
    connected=models.BooleanField(null=False,blank=False,default=False)
    model=models.CharField(choices=TypePrinter.choices,default=TypePrinter.OTHER)
    class Meta:
        verbose_name='Drukarka Etykiet'
        verbose_name_plural='Drukarki Etykiet'
        db_table='db_drukarki'
    
class Label(models.Model):
    name=models.CharField(max_length=100
                        ,null=False
                        ,blank=False
                        ,unique=True
                        ,validators=[
                            MinLengthValidator(10)
                        ])
    pattern=models.TextField(null=False
                            ,blank=False
                            ,default=""
                            ,max_length=2000
                            ,validators=[
                                MinLengthValidator(10)
                            ])
    class Meta:
        verbose_name='Etykieta'
        verbose_name_plural='Etykiety'
        db_table='db_etykiety'
