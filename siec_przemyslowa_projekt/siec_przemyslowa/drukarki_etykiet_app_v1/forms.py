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

class PrintForm(forms.Form):
    printer = forms.ModelChoiceField(queryset=models.Printer.objects.all())
    label = forms.ModelChoiceField(queryset=models.Label.objects.all())

class PrintFormScanner(forms.Form):
    printer = forms.ModelChoiceField(queryset=models.Printer.objects.all())
    label = forms.ModelChoiceField(queryset=models.Label.objects.all())
    barcode = forms.CharField(
        label="Kod ze skanera",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Zeskanuj kod...",
            "autofocus": True,
        })
    )