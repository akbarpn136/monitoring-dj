from __future__ import absolute_import

from django.core import serializers

import numpy as np
import scipy.fftpack as ft
from scipy.stats import exponweib
from monitor.celery import app

from .models import DataAngin
from .tambahan import gen_hex_colour_code, butter_bandpass_filter


@app.task
def do_angin(dt_frm, dt_to):
    temp_output = serializers.serialize('json', DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to),
                                        fields=('tanggal', 'waktu', 'arah', 'kecepatan', 'akselerator5'))

    return temp_output


@app.task
def do_windrose(dt_frm, dt_to, vmax, step):
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

    return k


@app.task
def do_pdf(dt_frm, dt_to):
    grp_v = DataAngin.objects.filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).order_by('kecepatan')

    list_kecepatan = np.array([o.grup_kecepatan for o in grp_v])
    # mean = np.mean(list_kecepatan)
    stddev = np.std(list_kecepatan, ddof=1)
    shape_k = (0.9874 / stddev) ** 1.0983
    x = 1 + (1 / shape_k)  # refeerence http://www.wind-power-program.com/wind_statistics.htm#top
    shape_gamma = 0.1693 * x ** 4 - 1.1495 * x ** 3 + 3.3005 * x ** 2 - 4.393 * x + 3.0726
    list_kecepatan_norm = exponweib.pdf(list_kecepatan,
                                        *exponweib.fit(list_kecepatan, shape_gamma, shape_k, scale=0.0, loc=0.0))

    dist_kecepatan = list_kecepatan.tolist()
    dist_kecepatan_norm = list_kecepatan_norm.tolist()

    obj = [{
        'velo': dist_kecepatan,
        'veloy': dist_kecepatan_norm,
    }]

    return obj


@app.task
def do_wtr(dt_frm, dt_to, grup, step, kompas='TM'):
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

    return obj


@app.task
def do_rms(vmax=1, step=0.1, kompas='all'):
    data_rms = {}
    x = []
    y = []

    for lop in np.arange(0, float(vmax), float(step)):
        if kompas == 'all':
            data_acc_1 = DataAngin.objects.filter(kecepatan__gte=lop,
                                                  kecepatan__lt=lop + float(step)).values_list('akselerator1',
                                                                                               flat=True)
        else:
            data_acc_1 = DataAngin.objects.filter(kecepatan__gte=lop, kecepatan__lt=lop + float(step),
                                                  kompas=kompas).values_list('akselerator1', flat=True)
        if data_acc_1.count() > 0:
            np_data_acc_1 = np.array(data_acc_1)
        else:
            np_data_acc_1 = np.array((0, 0))

        if kompas == 'all':
            data_acc_2 = DataAngin.objects.filter(kecepatan__gte=lop,
                                                  kecepatan__lt=lop + float(step)).values_list('akselerator2',
                                                                                               flat=True)
        else:
            data_acc_2 = DataAngin.objects.filter(kecepatan__gte=lop, kecepatan__lt=lop + float(step),
                                                  kompas=kompas).values_list('akselerator2', flat=True)
        if data_acc_2.count() > 0:
            np_data_acc_2 = np.array(data_acc_2)
        else:
            np_data_acc_2 = np.array((0, 0))

        if kompas == 'all':
            data_acc_3 = DataAngin.objects.filter(kecepatan__gte=lop,
                                                  kecepatan__lt=lop + float(step)).values_list('akselerator3',
                                                                                               flat=True)
        else:
            data_acc_3 = DataAngin.objects.filter(kecepatan__gte=lop, kecepatan__lt=lop + float(step),
                                                  kompas=kompas).values_list('akselerator3', flat=True)
        if data_acc_3.count() > 0:
            np_data_acc_3 = np.array(data_acc_3)
        else:
            np_data_acc_3 = np.array((0, 0))

        if kompas == 'all':
            data_acc_4 = DataAngin.objects.filter(kecepatan__gte=lop,
                                                  kecepatan__lt=lop + float(step)).values_list('akselerator4',
                                                                                               flat=True)
        else:
            data_acc_4 = DataAngin.objects.filter(kecepatan__gte=lop, kecepatan__lt=lop + float(step),
                                                  kompas=kompas).values_list('akselerator4', flat=True)
        if data_acc_4.count() > 0:
            np_data_acc_4 = np.array(data_acc_4)
        else:
            np_data_acc_4 = np.array((0, 0))

        if kompas == 'all':
            data_acc_5 = DataAngin.objects.filter(kecepatan__gte=lop,
                                                  kecepatan__lt=lop + float(step)).values_list('akselerator5',
                                                                                               flat=True)
        else:
            data_acc_5 = DataAngin.objects.filter(kecepatan__gte=lop, kecepatan__lt=lop + float(step),
                                                  kompas=kompas).values_list('akselerator5', flat=True)
        if data_acc_5.count() > 0:
            np_data_acc_5 = np.array(data_acc_5)
        else:
            np_data_acc_5 = np.array((0, 0))

        np_data_acc = np.concatenate((np_data_acc_1, np_data_acc_2, np_data_acc_3, np_data_acc_4, np_data_acc_5))
        np_data_acc_square = np.square(np_data_acc)
        np_data_acc_mean = np.mean(np_data_acc_square)
        np_data_acc_root = np.sqrt(np_data_acc_mean)
        nama_grup_kecepatan = str(lop) + ' - ' + str(lop + float(step))

        y.append(float(np_data_acc_root))
        x.append(str(nama_grup_kecepatan))

    data_rms['data_x'] = x
    data_rms['data_y'] = y

    return data_rms
