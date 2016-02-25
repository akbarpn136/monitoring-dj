from django.shortcuts import render, redirect, get_object_or_404

from .models import DaerahObjek, PilihanVisualisasi

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def index(request, pk=None):
    if pk is None:
        return redirect('halaman_utama_pk', 1)
    else:
        data_visualisasi = PilihanVisualisasi.objects.filter(daerah=pk)
        data = {
            'daerah': data_daerah,
            'daerah_pk': pk,
            'visualisasi': data_visualisasi,
        }

    return render(request, 'master/base.html', data)


def visual(request, pk):
    data_visual = get_object_or_404(PilihanVisualisasi, pk=pk)

    data = {
        'daerah': data_daerah,
        'visual': data_visual,
    }

    return render(request, 'monitoring/visual.html', data)
