from django.shortcuts import render, redirect

from .models import DaerahObjek


# Create your views here.
def index(request, pk=None):
    if pk is None:
        return redirect('halaman_utama_pk', 1)
    else:
        data_daerah = DaerahObjek.objects.all()
        data = {
            'daerah': data_daerah
        }

    return render(request, 'master/base.html', data)
