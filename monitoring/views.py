from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core import serializers

from scipy.stats import exponweib

from .models import DaerahObjek, PilihanVisualisasi, DataAngin

import json
import random
import numpy as np

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def gen_hex_colour_code():
    return ''.join([random.choice('0123456789ABCDEF') for x in range(6)])


def json_atr_angin(request, pk, dt_frm, dt_to):
    temp_output = serializers.serialize('json', DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm,
                                                                                           tanggal__lte=dt_to),
                                        fields=('tanggal', 'waktu', 'arah', 'kecepatan', 'akselerator5'))
    return HttpResponse(temp_output, content_type='application/json')


def json_rose_angin(request, pk, dt_frm, dt_to, vmax=7, step=0.5):
    grp_v_tot = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).count()

    if grp_v_tot > 0:
        k = {}
        for lop in np.arange(0, float(vmax), float(step)):
            grp_v_i = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
                .filter(grup_kecepatan__gte=lop, grup_kecepatan__lt=lop + 0.5)

            grp_v_i_ut = (grp_v_i.filter(kompas='UT').count() / grp_v_tot) * 100
            grp_v_i_tl = (grp_v_i.filter(kompas='TL').count() / grp_v_tot) * 100
            grp_v_i_tm = (grp_v_i.filter(kompas='TM').count() / grp_v_tot) * 100
            grp_v_i_tg = (grp_v_i.filter(kompas='TG').count() / grp_v_tot) * 100
            grp_v_i_sl = (grp_v_i.filter(kompas='SL').count() / grp_v_tot) * 100
            grp_v_i_bd = (grp_v_i.filter(kompas='BD').count() / grp_v_tot) * 100
            grp_v_i_br = (grp_v_i.filter(kompas='BR').count() / grp_v_tot) * 100
            grp_v_i_bl = (grp_v_i.filter(kompas='BL').count() / grp_v_tot) * 100

            list_grp_v_i = [grp_v_i_ut, grp_v_i_tl, grp_v_i_tm, grp_v_i_tg, grp_v_i_sl, grp_v_i_bd,
                            grp_v_i_br, grp_v_i_bl, str(lop)+'-'+str(lop+0.5)+' m/s']

            k[gen_hex_colour_code()] = list_grp_v_i

    else:
        k = {}

    return HttpResponse(json.dumps(k), content_type='application/json')


def json_pdf_angin(request, pk, dt_frm, dt_to):
    grp_v = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).order_by('kecepatan')

    list_kecepatan = np.array([o.kecepatan for o in grp_v])
    mean = np.mean(list_kecepatan)
    list_kecepatan_norm = exponweib.pdf(list_kecepatan, *exponweib.fit(list_kecepatan, 1, mean, scale=0, loc=0))

    dist_kecepatan = list_kecepatan.tolist()
    dist_kecepatan_norm = list_kecepatan_norm.tolist()

    obj = [{
        'velo': dist_kecepatan,
        'veloy': dist_kecepatan_norm,
    }]

    return HttpResponse(json.dumps(obj), content_type='application/json')


def json_wtr_angin(request, pk, dt_frm, dt_to):
    grp_v = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).order_by('kecepatan')

    grp_v_0_05 = grp_v.filter(kecepatan__gte=0, kecepatan__lt=0.5)
    grp_v_05_1 = grp_v.filter(kecepatan__gte=0.5, kecepatan__lt=1)
    grp_v_1_15 = grp_v.filter(kecepatan__gte=1, kecepatan__lt=1.5)
    grp_v_15_2 = grp_v.filter(kecepatan__gte=1.5, kecepatan__lt=2)
    grp_v_2_25 = grp_v.filter(kecepatan__gte=2, kecepatan__lt=2.5)
    grp_v_25_3 = grp_v.filter(kecepatan__gte=2.5, kecepatan__lt=3)
    grp_v_3_35 = grp_v.filter(kecepatan__gte=3, kecepatan__lt=3.5)
    grp_v_35_4 = grp_v.filter(kecepatan__gte=3.5, kecepatan__lt=4)
    grp_v_4_45 = grp_v.filter(kecepatan__gte=4, kecepatan__lt=4.5)
    grp_v_45_5 = grp_v.filter(kecepatan__gte=4.5, kecepatan__lt=5)
    grp_v_5_55 = grp_v.filter(kecepatan__gte=5, kecepatan__lt=5.5)
    grp_v_55_6 = grp_v.filter(kecepatan__gte=5.5, kecepatan__lt=6)
    grp_v_6_65 = grp_v.filter(kecepatan__gte=6, kecepatan__lt=6.5)
    grp_v_65_7 = grp_v.filter(kecepatan__gte=6.5, kecepatan__lt=7)

    list_kecepatan = np.array([o.kecepatan for o in grp_v])
    list_kecepatan_norm = exponweib.pdf(list_kecepatan, *exponweib.fit(list_kecepatan, 1, 1, scale=2, loc=0))

    dist_kecepatan = list_kecepatan.tolist()
    dist_kecepatan_norm = list_kecepatan_norm.tolist()

    obj = [{
        'velo': dist_kecepatan,
        'veloy': dist_kecepatan_norm,
    }]

    return HttpResponse(json.dumps(obj), content_type='application/json')


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


def visual(request, pk, daerah):
    data_visual = get_object_or_404(PilihanVisualisasi, pk=pk)

    data = {
        'daerah': data_daerah,
        'visual': data_visual,
        'daerah_tertentu': daerah
    }

    if data_visual.jenis == 'ATR':
        return render(request, 'monitoring/visual.html', data)
    elif data_visual.jenis == 'WRS':
        return render(request, 'monitoring/visual_windrose.html', data)
    elif data_visual.jenis == 'PDF':
        return render(request, 'monitoring/visual_pdf.html', data)
    else:
        pass
