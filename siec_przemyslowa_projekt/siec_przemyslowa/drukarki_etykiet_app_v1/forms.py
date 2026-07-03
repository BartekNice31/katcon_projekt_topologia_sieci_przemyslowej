from django import forms
from . import models

class PrinterForm(forms.ModelForm):
    class Meta:
        model=models.Printer
        fields = "__all__"

class LabelForm(forms.ModelForm):
    class Meta:
        model=models.Label
        fields="__all__"
