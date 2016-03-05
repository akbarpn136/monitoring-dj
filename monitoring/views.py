from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core import serializers
from django.contrib import messages

from .models import DaerahObjek, PilihanVisualisasi, DataAngin
from .tambahan import gen_hex_colour_code

import json
import operator
import numpy as np
import scipy.fftpack as ft
from scipy.stats import exponweib

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def json_atr_angin(request, pk, dt_frm, dt_to):
    temp_output = serializers.serialize('json', DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm,
                                                                                           tanggal__lte=dt_to),
                                        fields=('tanggal', 'waktu', 'arah', 'kecepatan', 'akselerator5'))
    return HttpResponse(temp_output, content_type='application/json')


def json_rose_angin(request, pk, dt_frm, dt_to, vmax, step):
    grp_v_tot = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).count()

    if grp_v_tot > 0:
        k = {}
        count = 0
        for lop in np.arange(0, float(vmax), float(step)):
            grp_v_i = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
                .filter(grup_kecepatan__gte=lop, grup_kecepatan__lt=lop + float(step))

            grp_v_i_ut = (grp_v_i.filter(kompas='UT').count() / grp_v_tot) * 100
            grp_v_i_tl = (grp_v_i.filter(kompas='TL').count() / grp_v_tot) * 100
            grp_v_i_tm = (grp_v_i.filter(kompas='TM').count() / grp_v_tot) * 100
            grp_v_i_tg = (grp_v_i.filter(kompas='TG').count() / grp_v_tot) * 100
            grp_v_i_sl = (grp_v_i.filter(kompas='SL').count() / grp_v_tot) * 100
            grp_v_i_bd = (grp_v_i.filter(kompas='BD').count() / grp_v_tot) * 100
            grp_v_i_br = (grp_v_i.filter(kompas='BR').count() / grp_v_tot) * 100
            grp_v_i_bl = (grp_v_i.filter(kompas='BL').count() / grp_v_tot) * 100

            list_grp_v_i = [grp_v_i_ut, grp_v_i_tl, grp_v_i_tm, grp_v_i_tg, grp_v_i_sl, grp_v_i_bd,
                            grp_v_i_br, grp_v_i_bl, str(lop)+'-'+str(lop + float(step))+' m/s', str(count) +
                            gen_hex_colour_code()]

            count += 1
            k[str(count)] = list_grp_v_i

    else:
        k = {}

    k_sorted = sorted(k.items(), key=operator.itemgetter(0))
    return HttpResponse(json.dumps(dict(k_sorted)), content_type='application/json')


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


def json_wtr_angin(request, pk, dt_frm, dt_to, grup, step, kompas='TM'):
    grp_v = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to)

    obj = {}

    for i in np.arange(0, float(grup), float(step)):
        grp_v_i = grp_v.filter(kecepatan__gte=i, kecepatan__lt=i + float(step)).filter(kompas=kompas)

        grp_v_i_acc1 = grp_v_i.values_list('akselerator1', flat=True)
        grp_v_i_acc2 = grp_v_i.values_list('akselerator2', flat=True)
        grp_v_i_acc3 = grp_v_i.values_list('akselerator3', flat=True)
        grp_v_i_acc4 = grp_v_i.values_list('akselerator4', flat=True)
        grp_v_i_acc5 = grp_v_i.values_list('akselerator5', flat=True)

        arr_grp_v_i_acc = np.matrix([grp_v_i_acc1, grp_v_i_acc2, grp_v_i_acc3, grp_v_i_acc4, grp_v_i_acc5])
        z = arr_grp_v_i_acc.transpose()

        fs = 15/7   # sampling rate
        # ts = 1.0/fs  # sampling interval
        # t = np.arange(0, 2, ts)  # time vector

        # ff = 5   # frequency of the signal
        # y = np.sin(2*np.pi*ff*t)

        # n = len(y)  # length of the signal
        n = z.size  # length of the signal
        # k = np.arange(n)
        # ti = n/fs
        # frq = k/ti  # two sides frequency range
        # frq = frq[:n/2]  # one side frequency range

        freq = ft.fftfreq(n, 0.2)
        freq = freq[:n/2]

        zf = abs(ft.fft(z))  # fft computing and normalization
        zf = zf[:n/2]

        yf = [i+float(step)]*n

        nama = str(i)+'-'+str(i + float(step))
        warna = '#' + str(int(i))+gen_hex_colour_code()

        obj[str(int(i))] = [nama, warna, freq.tolist(), yf, zf.flatten().tolist()]

    obj_sorted = sorted(obj.items(), key=operator.itemgetter(0))
    return HttpResponse(json.dumps(dict(obj_sorted)), content_type='application/json')


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
    elif data_visual.jenis == 'WTR':
        return render(request, 'monitoring/visual_wtr.html', data)
    else:
        messages.warning(request, "Jenis grafik tidak ditemukan.")
        return redirect('halaman_utama')
