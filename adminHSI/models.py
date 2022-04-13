from django.db import models

class Soal (models.Model):
    question=models.TextField()
    option_one=models.CharField(max_length=200)
    option_two=models.CharField(max_length=200)
    option_three=models.CharField(max_length=200)
    option_four=models.CharField(max_length=200)
    kunci=models.CharField(max_length=1)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural='Soals'     

    
    