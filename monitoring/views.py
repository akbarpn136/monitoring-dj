from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core import serializers

from .models import DaerahObjek, PilihanVisualisasi, DataAngin

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def json_atr_angin(request, pk):
    temp_output = serializers.serialize('json', DataAngin.objects.filter(daerah=pk),
                                        fields=('tanggal', 'waktu', 'arah', 'kecepatan'))
    print(temp_output)
    return HttpResponse(temp_output, content_type='application/json')


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

    if data_visual.jenis == 'ATR':
        script = 'graph=document.getElementById("' + data_visual.jenis + '");' \
                 'Plotly.plot( graph, [{' \
                 'x: [1, 2, 3, 4, 5],' \
                 'y: [1, 2, 4, 8, 16] }], {' \
                 'margin: { t: 0 } } );'

    else:
        script = ''

    data = {
        'daerah': data_daerah,
        'visual': data_visual,
        'script': script
    }

    return render(request, 'monitoring/visual.html', data)
