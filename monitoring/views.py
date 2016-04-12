from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core import serializers
from django.contrib import messages

from .models import DaerahObjek, PilihanVisualisasi, DataAngin
from .tambahan import gen_hex_colour_code, butter_bandpass_filter

import json
import operator
import numpy as np
import scipy.fftpack as ft
from scipy.stats import exponweib

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def json_atr_angin(request, dt_frm, dt_to):
    temp_output = serializers.serialize('json', DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to),
                                        fields=('tanggal', 'waktu', 'arah', 'kecepatan', 'akselerator5'))
    return HttpResponse(temp_output, content_type='application/json')


def json_rose_angin(request, dt_frm, dt_to, vmax, step):
    grp_v_tot = DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).count()

    if grp_v_tot > 0:
        k = {}
        count = 0
        for lop in np.arange(0, float(vmax), float(step)):
            grp_v_i = DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
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
                            grp_v_i_br, grp_v_i_bl, str(lop) + '-' + str(lop + float(step)) + ' m/s', str(count) +
                            gen_hex_colour_code()]

            count += 1
            k[str(count)] = list_grp_v_i

    else:
        k = {}

    k_sorted = sorted(k.items(), key=operator.itemgetter(0))
    return HttpResponse(json.dumps(dict(k_sorted)), content_type='application/json')


def json_pdf_angin(request, dt_frm, dt_to):
    grp_v = DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).order_by('kecepatan')

    list_kecepatan = np.array([o.grup_kecepatan for o in grp_v])
    # mean = np.mean(list_kecepatan)
    stddev = np.std(list_kecepatan, ddof=1)
    shape_k = (0.9874 / stddev) ** 1.0983
    x = 1 + (1 / shape_k)  # refeerence http://www.wind-power-program.com/wind_statistics.htm#top
    shape_gamma = 0.1693 * x ** 4 - 1.1495 * x ** 3 + 3.3005 * x ** 2 - 4.393 * x + 3.0726
    list_kecepatan_norm = exponweib.pdf(list_kecepatan,
                                        *exponweib.fit(list_kecepatan, shape_gamma, shape_k, scale=0.05, loc=0.01))

    dist_kecepatan = list_kecepatan.tolist()
    dist_kecepatan_norm = list_kecepatan_norm.tolist()

    obj = [{
        'velo': dist_kecepatan,
        'veloy': dist_kecepatan_norm,
    }]

    return HttpResponse(json.dumps(obj), content_type='application/json')


def json_wtr_angin(request, dt_frm, dt_to, grup, step, kompas='TM'):
    grp_v = DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to)

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

        samp_rate = 0.2
        fs = 1 / samp_rate  # sampling rate
        fc1 = 0.1  # First Cutoff Frequency
        fc2 = 0.4  # Second Cutoff Frequency
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

        if n > 0:
            freq = ft.fftfreq(n, 0.2)
            freq = freq[:n / 2]

            z = butter_bandpass_filter(z, fc1, fc2, fs, order=5)
            zf = abs(ft.fft(z) / n)  # fft computing and normalization
            zf = zf[:n / 2]

            yf = [i + float(step)] * n

            nama = str(i) + '-' + str(i + float(step))
            warna = '#' + str(int(i)) + gen_hex_colour_code()

            obj[str(int(i))] = [nama, warna, freq.tolist(), yf, zf.flatten().tolist()]

    obj_sorted = sorted(obj.items(), key=operator.itemgetter(0))
    return HttpResponse(json.dumps(dict(obj_sorted)), content_type='application/json')


def json_rms_angin(request, vmax=1, step=0.1):
    data_rms = {}
    x = []
    y = []

    for lop in np.arange(0, float(vmax), float(step)):
        data_acc_1 = DataAngin.objects.filter(grup_kecepatan__gte=lop,
                                              grup_kecepatan__lt=lop + float(step)).values_list('akselerator1',
                                                                                                flat=True)
        np_data_acc_1 = np.array(data_acc_1)

        data_acc_2 = DataAngin.objects.filter(grup_kecepatan__gte=lop,
                                              grup_kecepatan__lt=lop + float(step)).values_list('akselerator2',
                                                                                                flat=True)
        np_data_acc_2 = np.array(data_acc_2)

        data_acc_3 = DataAngin.objects.filter(grup_kecepatan__gte=lop,
                                              grup_kecepatan__lt=lop + float(step)).values_list('akselerator3',
                                                                                                flat=True)
        np_data_acc_3 = np.array(data_acc_3)

        data_acc_4 = DataAngin.objects.filter(grup_kecepatan__gte=lop,
                                              grup_kecepatan__lt=lop + float(step)).values_list('akselerator4',
                                                                                                flat=True)
        np_data_acc_4 = np.array(data_acc_4)

        data_acc_5 = DataAngin.objects.filter(grup_kecepatan__gte=lop,
                                              grup_kecepatan__lt=lop + float(step)).values_list('akselerator5',
                                                                                                flat=True)
        np_data_acc_5 = np.array(data_acc_5)

        np_data_acc = np.concatenate((np_data_acc_1, np_data_acc_2, np_data_acc_3, np_data_acc_4, np_data_acc_5))
        np_data_acc_square = np.square(np_data_acc)
        np_data_acc_mean = np.mean(np_data_acc_square)
        np_data_acc_root = np.sqrt(np_data_acc_mean)
        nama_grup_kecepatan = str(lop)+' - '+str(lop+float(step))

        y.append(float(np_data_acc_root))
        x.append(str(nama_grup_kecepatan))

    data_rms['data_x'] = x
    data_rms['data_y'] = y

    return HttpResponse(json.dumps(data_rms), content_type='application/json')


def index(request):
    data_visualisasi = PilihanVisualisasi.objects.all()
    data = {
        'daerah': data_daerah,
        'visualisasi': data_visualisasi,
    }

    return render(request, 'master/base.html', data)


def visual(request, pk):
    data_visual = get_object_or_404(PilihanVisualisasi, pk=pk)

    data = {
        'daerah': data_daerah,
        'visual': data_visual,
    }

    if data_visual.jenis == 'ATR':
        return render(request, 'monitoring/visual.html', data)
    elif data_visual.jenis == 'WRS':
        return render(request, 'monitoring/visual_windrose.html', data)
    elif data_visual.jenis == 'PDF':
        return render(request, 'monitoring/visual_pdf.html', data)
    elif data_visual.jenis == 'WTR':
        return render(request, 'monitoring/visual_wtr.html', data)
    elif data_visual.jenis == 'RMS':
        return render(request, 'monitoring/visual_rms.html', data)
    else:
        messages.warning(request, "Jenis grafik tidak ditemukan.")
        return redirect('halaman_utama')
