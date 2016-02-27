from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core import serializers

from .models import DaerahObjek, PilihanVisualisasi, DataAngin

import json

data_daerah = DaerahObjek.objects.all()


# Create your views here.
def json_atr_angin(request, pk, dt_frm, dt_to):
    temp_output = serializers.serialize('json', DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm,
                                                                                           tanggal__lte=dt_to),
                                        fields=('tanggal', 'waktu', 'arah', 'kecepatan', 'akselerator5'))
    return HttpResponse(temp_output, content_type='application/json')


def json_rose_angin(request, pk, dt_frm, dt_to):
    grp_v_tot = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to).count()

    grp_v_0_05 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=0, grup_kecepatan__lt=0.5)

    grp_v_0_05_ut = (grp_v_0_05.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_0_05_tl = (grp_v_0_05.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_0_05_tm = (grp_v_0_05.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_0_05_tg = (grp_v_0_05.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_0_05_sl = (grp_v_0_05.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_0_05_bd = (grp_v_0_05.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_0_05_br = (grp_v_0_05.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_0_05_bl = (grp_v_0_05.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_0_05 = [grp_v_0_05_ut, grp_v_0_05_tl, grp_v_0_05_tm, grp_v_0_05_tg, grp_v_0_05_sl, grp_v_0_05_bd,
                       grp_v_0_05_br, grp_v_0_05_bl]

    grp_v_05_1 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=0.5, grup_kecepatan__lt=1)

    grp_v_05_1_ut = (grp_v_05_1.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_05_1_tl = (grp_v_05_1.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_05_1_tm = (grp_v_05_1.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_05_1_tg = (grp_v_05_1.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_05_1_sl = (grp_v_05_1.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_05_1_bd = (grp_v_05_1.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_05_1_br = (grp_v_05_1.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_05_1_bl = (grp_v_05_1.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_05_1 = [grp_v_05_1_ut, grp_v_05_1_tl, grp_v_05_1_tm, grp_v_05_1_tg, grp_v_05_1_sl, grp_v_05_1_bd,
                       grp_v_05_1_br, grp_v_05_1_bl]

    grp_v_1_15 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=1, grup_kecepatan__lt=1.5)

    grp_v_1_15_ut = (grp_v_1_15.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_1_15_tl = (grp_v_1_15.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_1_15_tm = (grp_v_1_15.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_1_15_tg = (grp_v_1_15.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_1_15_sl = (grp_v_1_15.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_1_15_bd = (grp_v_1_15.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_1_15_br = (grp_v_1_15.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_1_15_bl = (grp_v_1_15.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_1_15 = [grp_v_1_15_ut, grp_v_1_15_tl, grp_v_1_15_tm, grp_v_1_15_tg, grp_v_1_15_sl, grp_v_1_15_bd,
                       grp_v_1_15_br, grp_v_1_15_bl]

    grp_v_15_2 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=1.5, grup_kecepatan__lt=2)

    grp_v_15_2_ut = (grp_v_15_2.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_15_2_tl = (grp_v_15_2.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_15_2_tm = (grp_v_15_2.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_15_2_tg = (grp_v_15_2.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_15_2_sl = (grp_v_15_2.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_15_2_bd = (grp_v_15_2.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_15_2_br = (grp_v_15_2.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_15_2_bl = (grp_v_15_2.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_15_2 = [grp_v_15_2_ut, grp_v_15_2_tl, grp_v_15_2_tm, grp_v_15_2_tg, grp_v_15_2_sl, grp_v_15_2_bd,
                       grp_v_15_2_br, grp_v_15_2_bl]

    grp_v_2_25 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=2, grup_kecepatan__lt=2.5)

    grp_v_2_25_ut = (grp_v_2_25.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_2_25_tl = (grp_v_2_25.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_2_25_tm = (grp_v_2_25.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_2_25_tg = (grp_v_2_25.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_2_25_sl = (grp_v_2_25.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_2_25_bd = (grp_v_2_25.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_2_25_br = (grp_v_2_25.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_2_25_bl = (grp_v_2_25.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_2_25 = [grp_v_2_25_ut, grp_v_2_25_tl, grp_v_2_25_tm, grp_v_2_25_tg, grp_v_2_25_sl, grp_v_2_25_bd,
                       grp_v_2_25_br, grp_v_2_25_bl]

    grp_v_25_3 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=2.5, grup_kecepatan__lt=3)

    grp_v_25_3_ut = (grp_v_25_3.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_25_3_tl = (grp_v_25_3.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_25_3_tm = (grp_v_25_3.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_25_3_tg = (grp_v_25_3.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_25_3_sl = (grp_v_25_3.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_25_3_bd = (grp_v_25_3.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_25_3_br = (grp_v_25_3.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_25_3_bl = (grp_v_25_3.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_25_3 = [grp_v_25_3_ut, grp_v_25_3_tl, grp_v_25_3_tm, grp_v_25_3_tg, grp_v_25_3_sl, grp_v_25_3_bd,
                       grp_v_25_3_br, grp_v_25_3_bl]

    grp_v_3_35 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=3, grup_kecepatan__lt=3.5)

    grp_v_3_35_ut = (grp_v_3_35.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_3_35_tl = (grp_v_3_35.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_3_35_tm = (grp_v_3_35.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_3_35_tg = (grp_v_3_35.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_3_35_sl = (grp_v_3_35.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_3_35_bd = (grp_v_3_35.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_3_35_br = (grp_v_3_35.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_3_35_bl = (grp_v_3_35.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_3_35 = [grp_v_3_35_ut, grp_v_3_35_tl, grp_v_3_35_tm, grp_v_3_35_tg, grp_v_3_35_sl, grp_v_3_35_bd,
                       grp_v_3_35_br, grp_v_3_35_bl]

    grp_v_35_4 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=3.5, grup_kecepatan__lt=4)

    grp_v_35_4_ut = (grp_v_35_4.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_35_4_tl = (grp_v_35_4.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_35_4_tm = (grp_v_35_4.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_35_4_tg = (grp_v_35_4.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_35_4_sl = (grp_v_35_4.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_35_4_bd = (grp_v_35_4.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_35_4_br = (grp_v_35_4.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_35_4_bl = (grp_v_35_4.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_35_4 = [grp_v_35_4_ut, grp_v_35_4_tl, grp_v_35_4_tm, grp_v_35_4_tg, grp_v_35_4_sl, grp_v_35_4_bd,
                       grp_v_35_4_br, grp_v_35_4_bl]

    grp_v_4_45 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=4, grup_kecepatan__lt=4.5)

    grp_v_4_45_ut = (grp_v_4_45.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_4_45_tl = (grp_v_4_45.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_4_45_tm = (grp_v_4_45.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_4_45_tg = (grp_v_4_45.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_4_45_sl = (grp_v_4_45.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_4_45_bd = (grp_v_4_45.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_4_45_br = (grp_v_4_45.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_4_45_bl = (grp_v_4_45.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_4_45 = [grp_v_4_45_ut, grp_v_4_45_tl, grp_v_4_45_tm, grp_v_4_45_tg, grp_v_4_45_sl, grp_v_4_45_bd,
                       grp_v_4_45_br, grp_v_4_45_bl]

    grp_v_45_5 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=4.5, grup_kecepatan__lt=5)

    grp_v_45_5_ut = (grp_v_45_5.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_45_5_tl = (grp_v_45_5.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_45_5_tm = (grp_v_45_5.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_45_5_tg = (grp_v_45_5.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_45_5_sl = (grp_v_45_5.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_45_5_bd = (grp_v_45_5.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_45_5_br = (grp_v_45_5.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_45_5_bl = (grp_v_45_5.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_45_5 = [grp_v_45_5_ut, grp_v_45_5_tl, grp_v_45_5_tm, grp_v_45_5_tg, grp_v_45_5_sl, grp_v_45_5_bd,
                       grp_v_45_5_br, grp_v_45_5_bl]

    grp_v_5_55 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=5, grup_kecepatan__lt=5.5)

    grp_v_5_55_ut = (grp_v_5_55.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_5_55_tl = (grp_v_5_55.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_5_55_tm = (grp_v_5_55.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_5_55_tg = (grp_v_5_55.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_5_55_sl = (grp_v_5_55.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_5_55_bd = (grp_v_5_55.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_5_55_br = (grp_v_5_55.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_5_55_bl = (grp_v_5_55.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_5_55 = [grp_v_5_55_ut, grp_v_5_55_tl, grp_v_5_55_tm, grp_v_5_55_tg, grp_v_5_55_sl, grp_v_5_55_bd,
                       grp_v_5_55_br, grp_v_5_55_bl]

    grp_v_55_6 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=5.5, grup_kecepatan__lt=6)

    grp_v_55_6_ut = (grp_v_55_6.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_55_6_tl = (grp_v_55_6.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_55_6_tm = (grp_v_55_6.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_55_6_tg = (grp_v_55_6.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_55_6_sl = (grp_v_55_6.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_55_6_bd = (grp_v_55_6.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_55_6_br = (grp_v_55_6.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_55_6_bl = (grp_v_55_6.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_55_6 = [grp_v_55_6_ut, grp_v_55_6_tl, grp_v_55_6_tm, grp_v_55_6_tg, grp_v_55_6_sl, grp_v_55_6_bd,
                       grp_v_55_6_br, grp_v_55_6_bl]

    grp_v_6_60 = DataAngin.objects.filter(daerah=pk).filter(tanggal__gte=dt_frm, tanggal__lte=dt_to) \
        .filter(grup_kecepatan__gte=6)

    grp_v_6_60_ut = (grp_v_6_60.filter(kompas='UT').count() / grp_v_tot) * 100
    grp_v_6_60_tl = (grp_v_6_60.filter(kompas='TL').count() / grp_v_tot) * 100
    grp_v_6_60_tm = (grp_v_6_60.filter(kompas='TM').count() / grp_v_tot) * 100
    grp_v_6_60_tg = (grp_v_6_60.filter(kompas='TG').count() / grp_v_tot) * 100
    grp_v_6_60_sl = (grp_v_6_60.filter(kompas='SL').count() / grp_v_tot) * 100
    grp_v_6_60_bd = (grp_v_6_60.filter(kompas='BD').count() / grp_v_tot) * 100
    grp_v_6_60_br = (grp_v_6_60.filter(kompas='BR').count() / grp_v_tot) * 100
    grp_v_6_60_bl = (grp_v_6_60.filter(kompas='BL').count() / grp_v_tot) * 100

    list_grp_v_6_60 = [grp_v_6_60_ut, grp_v_6_60_tl, grp_v_6_60_tm, grp_v_6_60_tg, grp_v_6_60_sl, grp_v_6_60_bd,
                       grp_v_6_60_br, grp_v_6_60_bl]

    obj = [{
        'trace1': list_grp_v_0_05,
        'trace2': list_grp_v_05_1,
        'trace3': list_grp_v_1_15,
        'trace4': list_grp_v_15_2,
        'trace5': list_grp_v_2_25,
        'trace6': list_grp_v_25_3,
        'trace7': list_grp_v_3_35,
        'trace8': list_grp_v_35_4,
        'trace9': list_grp_v_4_45,
        'trace10': list_grp_v_45_5,
        'trace11': list_grp_v_5_55,
        'trace12': list_grp_v_55_6,
        'trace13': list_grp_v_6_60,
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
    else:
        pass
