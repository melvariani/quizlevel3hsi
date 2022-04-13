from django.urls import path
from adminHSI import views as av
from PesertaHSI import views as pv 

urlpatterns = [
    path('', av.index,name="home"),
    path('pesertaHSI/',pv.halPeserta, name="halPeserta"),
    path('EvaluasiHarian/',pv.soalUjian, name="soalUjian"),
    path('HasilPeserta/',pv.hasil, name="hasilpeserta"),
    # path('buatsoal/',views.addsoal, name="buatsoal"),
    # path('ubahsoal/<soal_id>/',views.editSoal, name="ubahsoal"),
    # path('hapussoal/<soal_id>/',views.deleteSoal, name="hapussoal")
]





