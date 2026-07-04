from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from . import utils
from . import models
from . import forms
from . import utils
from . import print_label_program
import socket
# Create your views here.

def printers_home_page(request):
    return render(request,'printers_home_page.html')

def database_printers_page(request):
    printers=models.Printer.objects.all()
    for printer in printers:
        printer.connected=utils.is_device_online(printer.ip)
        printer.save()
    print(printers)
    return render(request,'database_printers.html',{'data':printers})

def show_printers_page(request):
    printers=models.Printer.objects.all()
    print(printers)
    for printer in printers:
        printer.connected=utils.is_device_online(printer.ip)
        printer.save()
    return render(request,'database_printers_page.html',{'data':printers})

def add_new_printer(request):
    if request.method=="POST":
        form=forms.PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('database_printers_page')
    else:
        form=forms.PrinterForm()
    return render(request,'add_new_printer.html',{"form":form})

def edit_printer(request,id):
    printer_to_edit=models.Printer.objects.get(id=id)
    if request.method=="POST":
        form=forms.PrinterForm(request.POST,instance=printer_to_edit)
        form.save()
        return redirect('database_printers_page')
    else:
        form=forms.PrinterForm(instance=printer_to_edit)
    return render(
        request
        ,'edit_printer.html'
        ,{'form':form}
    )

def remove_printer(request,id):
    printer_to_remove=models.Printer.objects.get(id=id)
    printer_to_remove.delete()
    return redirect('database_printers_page')

def database_labels(request):
    labels=models.Label.objects.all()
    return render(request,'templates_labels/database_labels.html',{'data':labels})

def add_new_label(request):
    if request.method=="POST":
        form=forms.LabelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database_labels')
    else:
        form=forms.LabelForm()
    return render(request,'templates_labels/add_new_label.html',{"form":form})

def edit_label(request,id):
    label_to_edit=models.Label.objects.get(id=id)
    if request.method=="POST":
        form=forms.LabelForm(request.POST,instance=label_to_edit)
        form.save()
        return redirect('database_labels')
    else:
        form=forms.LabelForm(instance=label_to_edit)
    return render(
        request
        ,'templates_labels/edit_label.html'
        ,{'form':form}
    )

def delete_label(request,id):
    label_to_remove=models.Label.objects.get(id=id)
    label_to_remove.delete()
    return redirect('database_labels')

def print_label(request):
    form = forms.PrintForm()
    if request.method == "POST":
        form = forms.PrintForm(request.POST)
        if form.is_valid():
            printer = form.cleaned_data["printer"]
            label = form.cleaned_data["label"]

            # 🔥 TU LOGIKA DRUKU (na razie print)
            print(f"DRUKUJĘ {label.name} na {printer.name} o adresie: {printer.ip}")
            print_label_program.print_label(zpl=label.pattern,printer_ip=printer.ip,port=9100)
            # tutaj później np. ZPL / socket / API drukarki
            return render(request, "templates_printers/print_label.html", {
                "form": form,
                "message": "Wysłano do drukarki ✔"
            }) 

    return render(request, "templates_printers/print_label.html", {"form": form})

def print_label_from_zebra(request):
    form = forms.PrintFormScanner()
    if request.method == "POST":
        form = forms.PrintFormScanner(request.POST)
        if form.is_valid():
            printer = form.cleaned_data["printer"]
            label = form.cleaned_data["label"]
            barcode = form.cleaned_data["barcode"]

            # 🔥 TU LOGIKA DRUKU (na razie print)
            print(f"DRUKUJĘ {label.name} na {printer.name} o adresie: {printer.ip}")
            print(label.pattern.replace('**Wpisz_tutaj**',barcode))
            # print_label_program.print_label(zpl=label.pattern.replace('**Wpisz_tutaj**',barcode),printer_ip=printer.ip,port=9100)
            # tutaj później np. ZPL / socket / API drukarki
            return render(request, "templates_printers/print_label_zebra_scanner.html", {
                "form": form,
                "message": "Wysłano do drukarki ✔"
            }) 

    return render(request, "templates_printers/print_label_zebra_scanner.html", {"form": form})