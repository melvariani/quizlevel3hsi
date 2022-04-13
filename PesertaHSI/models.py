from django.db import models
from adminHSI.models import Soal

# class Peserta (models.Model):
#     peserta_NIP=models.CharField(max_length=20)
#     Peserta_Name=models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.peserta_NIP

class Soal_Peserta(models.Model):
    # Peserta_ID=models.ForeignKey(Peserta, on_delete=models.CASCADE)
    # 
    Paket_Soal_ID=models.CharField(max_length=10,null=True)
    Soal_ID=models.TextField(null=True)
    option_one=models.CharField(max_length=200,null=True)
    option_two=models.CharField(max_length=200,null=True)
    option_three=models.CharField(max_length=200,null=True)
    option_four=models.CharField(max_length=200,null=True)
    kunci=models.CharField(max_length=1,null=True)
    Choice=models.CharField(max_length=1,null=True)
    Status=models.BooleanField(default=False)
    Nilai=models.IntegerField(null=True)
    Total=models.IntegerField(null=True)
    
    def __str__(self):
         return self.Paket_Soal_ID
     

    
