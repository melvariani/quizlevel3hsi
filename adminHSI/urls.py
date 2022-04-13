from django.urls import path
from adminHSI import views as av
from PesertaHSI import views as pv 

urlpatterns = [
    path('', av.index,name="home"),
    path('adminHSI/',av.HaladminHsi, name="halAdmin"),
    path('banksoal/',av.banksoal, name="kumpulansoal"),
    path('buatsoal/',av.addsoal, name="buatsoal"),
    path('ubahsoal/<soal_id>/',av.editSoal, name="ubahsoal"),
    path('hapussoal/<soal_id>/',av.deleteSoal, name="hapussoal"),
    path('pesertaHSI/',pv.halPeserta, name="halPeserta"),
    path('EvaluasiHarian/',pv.soalUjian, name="soalUjian"),
    path('HasilPeserta/',pv.hasil, name="hasilpeserta")
    
]





