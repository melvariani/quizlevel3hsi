from django import forms
from django.forms import ModelForm
from .models import Soal


class CreateSoalForm(ModelForm):
    
    question=forms.CharField(max_length=400,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Pertanyaan"}),label="")   
    option_one=forms.CharField(max_length=400,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pilihan 1'}),label="")
    option_two=forms.CharField(max_length=400,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pilihan 2'}),label="")
    option_three=forms.CharField(max_length=400,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pilihan 3'}),label="")
    option_four=forms.CharField(max_length=400,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pilihan 4'}),label="")
    kunci=forms.CharField(max_length=1,widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Kunci Jawaban (A/B/C/D)','maxlength':"1",}),label="")
    
    class Meta :
        model=Soal
        fields=('question','option_one','option_two','option_three','option_four','kunci')
        
        