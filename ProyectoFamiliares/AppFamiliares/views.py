from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from AppFamiliares.models import *


def familiares(request):
    fam1 = Familiar(nombre="Alicia", clase="Madre", edad=70, fechaNacimiento="1943-9-12")
    fam1.save()
    fam2 = Familiar(nombre="Hugo", clase="Padre", edad=74, fechaNacimiento="1938-10-14")
    fam2.save()
    fam3 = Familiar(nombre="Valeria", clase="Hermana", edad=42, fechaNacimiento="1988-03-04")
    fam3.save()

    familia = Familiar.objects.all()
    cxt = {"familia": familia}
    print(familia)
    return render(request, "AppFamiliares/listadefamiliares.html",cxt )
    

