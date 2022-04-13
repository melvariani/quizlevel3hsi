from django.shortcuts import render,redirect
from adminHSI.models import Soal
from random import random
import random
from .models import Soal_Peserta


def halPeserta(request):
    return render(request,'pesertaHSI/halPeserta.html')

def soalUjian(request):
    if request.method== "GET" :
        soals=Soal.objects.all().order_by('?')[:2]
        context={
            'soals':soals
        }
        return render(request,'pesertaHSI/soalUjian.html',context)
    if request.method=="POST":
        data=request.POST
        if data['Choice1']==data["key1"] :
            Stat1=True
            Nilai1=2
        else :
            Stat1=False
            Nilai1=1
        
        if data['Choice2']==data["key2"] :
            Stat2=True
            Nilai2=2
        else :
            Stat2=False
            Nilai2=1
        TotalNilai=Nilai1+Nilai2
        Count_Paket=int(Soal_Peserta.objects.count()/2)
        Paket_ID="EV" + str(Count_Paket+1)
        ret=Soal_Peserta.objects.create(Paket_Soal_ID=Paket_ID,Soal_ID=data['soal1'],
                                        option_one= data['Pilihan11'],option_two= data['Pilihan21'],
                                        option_three= data['Pilihan31'],option_four= data['Pilihan41'],
                                        kunci=data['key1'],
                                        Choice=data['Choice1'],Status=Stat1,Nilai=Nilai1,Total=TotalNilai)
        ret=Soal_Peserta.objects.create(Paket_Soal_ID=Paket_ID,Soal_ID=data['soal2'],
                                        option_one= data['Pilihan12'],option_two= data['Pilihan22'],
                                        option_three= data['Pilihan32'],option_four= data['Pilihan42'],
                                        kunci=data['key2'],
                                        Choice=data['Choice2'],Status=Stat2,Nilai=Nilai2,Total=TotalNilai)
        return redirect('halPeserta')

def hasil(request):
    if request.method== "GET" :
        HslEva=Soal_Peserta.objects.all()
        context={
            'HslEva':HslEva
        }
        
    return render(request,'pesertaHSI/HasilPeserta.html',context)