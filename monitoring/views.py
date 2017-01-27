from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.core import serializers

from .models import DaerahObjek, PilihanVisualisasi, DataAngin
from .tambahan import conv_timestamp, gen_hex_colour_code
from .tasks import do_windrose, do_pdf, do_wtr, do_angin, do_rms

import numpy as np
import datetime
import json
import operator

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def json_atr_angin(request, dt_frm, dt_to):
    task_result = do_angin.delay(dt_frm, dt_to)
    obj = task_result.get()

    return HttpResponse(obj, content_type='application/json')


def json_rose_angin(request, dt_frm, dt_to, vmax, step):
    # task_result = do_windrose.delay(dt_frm, dt_to, vmax, step)

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
        
    # k_sorted = sorted(task_result.get().items(), key=operator.itemgetter(0))
    # k_sorted = sorted(k, key=operator.itemgetter(0))
    
    return HttpResponse(json.dumps(k, sort_keys=True), content_type='application/json')


def json_pdf_angin(request, dt_frm, dt_to):
    task_result = do_pdf.delay(dt_frm, dt_to)

    obj = task_result.get()

    return HttpResponse(json.dumps(obj), content_type='application/json')


def json_wtr_angin(request, dt_frm, dt_to, grup, step, kompas='TM'):
    task_result = do_wtr.delay(dt_frm, dt_to, grup, step, kompas)

    obj = task_result.get()

    obj_sorted = sorted(obj.items(), key=operator.itemgetter(0))
    return HttpResponse(json.dumps(dict(obj_sorted)), content_type='application/json')


def json_rms_angin(request, vmax=1, step=0.1, kompas='all'):
    task_result = do_rms.delay(vmax, step, kompas)
    data_rms = task_result.get()

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


def realtime(request):
    date_time = datetime.datetime.now()  # millisecond
    data_x = []
    data_y_kec = []
    data_y_arh = []
    data_y_gtr = []

    for i in range(-20, 0):
        data_x.append(int((date_time + datetime.timedelta(seconds=i*3)).timestamp() * 1e3))

    for j in data_x:
        tanggal = conv_timestamp(j/1e3).date()
        waktu = conv_timestamp(j/1e3).time()
        dt_kec = DataAngin.objects.filter(tanggal=tanggal, waktu=waktu).values_list('kecepatan', flat=True)
        dt_arh = DataAngin.objects.filter(tanggal=tanggal, waktu=waktu).values_list('arah', flat=True)
        dt_acc = DataAngin.objects.filter(tanggal=tanggal, waktu=waktu).values_list('akselerator5', flat=True)

        if dt_kec.count() == 0:
            dt_kec = 0
        if dt_arh.count() == 0:
            dt_arh = 0
        if dt_acc.count() == 0:
            dt_acc = 0

        data_y_kec.append(dt_kec)
        data_y_arh.append(dt_arh)
        data_y_gtr.append(dt_acc)

    data = {
        'data_x': data_x,
        'data_y_kec': data_y_kec,
        'data_y_arh': data_y_arh,
        'data_y_gtr': data_y_gtr,
    }

    return render(request, 'monitoring/visual_rltm.html', data)


def get_rltm_dt(request, jns, ms):
    s = datetime.datetime.fromtimestamp(int(ms) / 1000)
    tanggal = s.date()
    waktu = s.strftime('%H:%M:%S')

    if jns == 'kec':
        data = serializers.serialize('json', DataAngin.objects.filter(tanggal=tanggal, waktu=waktu),
                                     fields='kecepatan')

    elif jns == 'arh':
        data = serializers.serialize('json', DataAngin.objects.filter(tanggal=tanggal, waktu=waktu),
                                     fields='arah')

    else:
        data = serializers.serialize('json', DataAngin.objects.filter(tanggal=tanggal, waktu=waktu),
                                     fields='akselerator5')

    return HttpResponse(data, content_type='application/json')
