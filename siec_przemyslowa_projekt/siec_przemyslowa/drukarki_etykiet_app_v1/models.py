from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

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
                    ,validators=[
                        MinLengthValidator(7)
                    ])
    connected=models.BooleanField(null=False,blank=False,default=False)
    class Meta:
        verbose_name='Drukarka Etykiet'
        verbose_name_plural='Drukarki Etykiet'
        db_table='db_drukarki'
    
class Label(models.Model):
    name=models.CharField(max_length=100
                        ,null=False
                        ,blank=False
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
