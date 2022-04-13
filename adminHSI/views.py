from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Soal
from .forms import CreateSoalForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request,'adminHSI/index.html')

def HaladminHsi(request):
    return render(request,'adminHSI/homeAdmin.html')

def banksoal(request):
    soals=Soal.objects.all()
    context={
        'soals':soals
    }
    return render(request,'adminHSI/soal.html',context)

# def addsoal(request):
#     if request.method=='POST':
#         form=CreateSoalForm(request.POST)
#         if form.is_valid() :
#             form.save()
#             return redirect('kumpulansoal')
#     else :
#         form=CreateSoalForm()
#     context={
#         'form' : form 
#     }
#     return render(request,'adminHSI/createSoal.html',context)

def addsoal(request):
    submitted=False
    if request.method=='POST':
        # form=CreateSoalForm(request.POST)
        # if form.is_valid() :
        #     form.save()
        #     return HttpResponseRedirect('/buatsoal?submitted=True')
        data=request.POST
        ret=Soal.objects.create(question=data['question'],
                                option_one= data['option_one'],option_two= data['option_two'],
                                        option_three= data['option_three'],option_four= data['option_four'],
                                        kunci=data['Kunci Jawaban'])
                                        
        # ret=Soal_Peserta.objects.create(Paket_Soal_ID=Paket_ID,Choice=data['Choice1'],Status=Stat1,Nilai=Nilai1)
        # ret=Soal_Peserta.objects.create(Paket_Soal_ID=Paket_ID,Choice=data['Choice2'],Status=Stat2,Nilai=Nilai2)
        return HttpResponseRedirect('/buatsoal?submitted=True') 
    else :
         form=CreateSoalForm()
         if 'submitted' in request.GET :
             submitted = True
    context={
         'form' : form,
         'submitted' : submitted 
    }
    return render(request,'adminHSI/createSoal.html',context)



def editSoal (request,soal_id):
    if request.method== "GET" :
    
        soal=Soal.objects.get(pk=soal_id)
        context={
                'soal':soal
            }
        return render(request,'adminHSI/editSoal.html',context)
 
    if request.method=="POST":
        data=request.POST
        ret=Soal.objects.get(pk=soal_id)
        
        
        ret.question=data['question']
        ret.option_one=data['option_one']
        ret.option_two=data['option_two']
        ret.option_three=data['option_three']
        ret.option_four=data['option_four']
        ret.kunci=data['Kunci Jawaban']
        ret.save()
        return redirect('kumpulansoal')
        
 
 
 
 
 
 

def deleteSoal (request,soal_id):
    try :
        soal=Soal.objects.get(pk=soal_id)
        soal.delete()
        return redirect('kumpulansoal')
    except ObjectDoesNotExist:
        return redirect('kumpulansoal')
    
    
