from django.shortcuts import render, redirect

from .models import DaerahObjek, PilihanVisualisasi


# Create your views here.
def index(request, pk=None):
    if pk is None:
        return redirect('halaman_utama_pk', 1)
    else:
        data_daerah = DaerahObjek.objects.all()
        data_visualisasi = PilihanVisualisasi.objects.filter(daerah=pk)
        data = {
            'daerah': data_daerah,
            'visualisasi': data_visualisasi
        }

    return render(request, 'master/base.html', data)
