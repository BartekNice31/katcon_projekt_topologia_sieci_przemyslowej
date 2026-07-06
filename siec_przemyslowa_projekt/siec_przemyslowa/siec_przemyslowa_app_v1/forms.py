from django import forms
from . import models

class LiniaProdukcyjnaForm(forms.ModelForm):
    class Meta:
        model=models.LiniaProdukcyjna
        fields = "__all__"

class MaszynaProdukcyjnaForm(forms.ModelForm):
    class Meta:
        model=models.MaszynaProdukcyjna
        fields = "__all__"

class UrzadzenieMaszynyForm(forms.ModelForm):
    class Meta:
        model=models.UrzadzenieMaszyny
        fields = "__all__"

class PLCMaszynyForm(forms.ModelForm):
    class Meta:
        model=models.PLCMaszyna
        fields="__all__"
