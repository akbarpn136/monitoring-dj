from __future__ import absolute_import

import numpy as np
from monitor.celery import app

from .models import DataAngin
from .tambahan import gen_hex_colour_code


@app.task
def add(x, y):
    return x + y


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
