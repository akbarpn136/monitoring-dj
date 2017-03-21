import json

import numpy
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import generics

from monitoring import models
from . import serializers
from .extras import DoFilter


# Create your views here.
class MonitorAngin(generics.ListCreateAPIView):
    queryset = models.DataAngin.objects.all()
    serializer_class = serializers.MonitorAnginSerializer

    def get_queryset(self):
        date_from = self.kwargs['date_from']
        date_to = self.kwargs['date_to']

        q = models.DataAngin.objects.filter(
            tanggal__gte=date_from,
            tanggal__lte=date_to
        )

        return q


class MonitorWindrose(ListView):
    def get_queryset(self):
        date_from = self.kwargs['date_from']
        date_to = self.kwargs['date_to']

        q = models.DataAngin.objects.filter(
            tanggal__gte=date_from,
            tanggal__lte=date_to
        )

        return q

    def get(self, request, *args, **kwargs):
        vmax = float(self.request.GET.get('vmax'))
        step = float(self.request.GET.get('step'))
        obj = self.do_task(vmax, step)

        return HttpResponse(json.dumps(obj, sort_keys=True), content_type='Applications/json')

    def do_task(self, vmax, step):
        v_range = numpy.arange(0.0, vmax + step, step).tolist()
        total = self.get_queryset().count()

        if total > 0:
            obj = [{
                       'id': i,
                       'persentase': [
                           (self.get_queryset().filter(kompas__contains='UT', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='TL', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='TM', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='TG', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='SL', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='BD', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='BR', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100,
                           (self.get_queryset().filter(kompas__contains='BL', grup_kecepatan__gte=v,
                                                       grup_kecepatan__lt=v + step).count() / total) * 100
                       ],
                       'nama': str(v)[0:3] + ' - ' + str(v + step)[0:3] + ' m/s',
                       'kompas': ['Utara', 'Timur Laut', 'Timur', 'Tenggara', 'Selatan', 'Barat Daya', 'Barat',
                                  'Barat Laut'],
                   } for i, v in enumerate(v_range)]
        else:

            obj = [{}]

        return obj


class MonitorRMS(ListView):
    def get(self, request, *args, **kwargs):
        vmax = float(self.request.GET.get('vmax'))
        step = float(self.request.GET.get('step'))
        arah = self.request.GET.get('arah')
        obj = self.do_task(vmax, step, arah)

        return HttpResponse(json.dumps([obj], sort_keys=True), content_type='Applications/json')

    @staticmethod
    def do_task(vmax, step, arah):
        v_range = numpy.arange(0.0, vmax, step).tolist()
        obj = {}
        data_x = []
        data_y = []

        for i, v in enumerate(v_range):
            v = round(v, 1)

            if arah == 'all':
                data_acc = models.DataAngin.objects.filter(
                    kecepatan__gte=v,
                    kecepatan__lt=v + step
                ).values_list(
                    'akselerator1', 'akselerator2', 'akselerator3', 'akselerator4', 'akselerator5'
                )
            else:
                data_acc = models.DataAngin.objects.filter(
                    kecepatan__gte=v,
                    kecepatan__lt=v + step,
                    kompas__contains=arah
                ).values_list(
                    'akselerator1', 'akselerator2', 'akselerator3', 'akselerator4', 'akselerator5'
                )

            numpy_data_acc = numpy.array(data_acc)
            numpy_data_acc_square = numpy.square(numpy_data_acc)
            numpy_data_acc_mean = numpy.mean(numpy_data_acc_square)
            numpy_data_acc_root = numpy.sqrt(numpy_data_acc_mean)

            data_x.append(str(v) + ' - ' + str(v + step))
            data_y.append(numpy_data_acc_root)

        obj['x'] = data_x
        obj['y'] = data_y

        return obj


class MonitorWaterfall(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wkt_akh = ''
        self.wkt_awl = ''
        self.arah = ''
        self.step = 0
        self.vmax = 0
        self.first_cutoff = 0.1
        self.second_cutoff = 0.4
        self.sample_spacing = 0.2
        self.order = 3
        self.do_filter = False

    def dispatch(self, request, *args, **kwargs):
        self.wkt_akh = self.request.GET.get('wkt_akhir')
        self.wkt_awl = self.request.GET.get('wkt_awal')
        self.arah = self.request.GET.get('arah')
        self.step = float(self.request.GET.get('step'))
        self.vmax = float(self.request.GET.get('vmax'))

        self.first_cutoff = float(self.request.GET.get('first_cutoff')) if self.request.GET.get(
            'first_cutoff') else self.first_cutoff

        self.second_cutoff = float(self.request.GET.get('second_cutoff')) if self.request.GET.get(
            'second_cutoff') else self.second_cutoff

        self.sample_spacing = float(self.request.GET.get('sample_spacing')) if self.request.GET.get(
            'sample_spacing') else self.sample_spacing

        self.order = float(self.request.GET.get('order')) if self.request.GET.get('order') else self.order
        self.do_filter = bool(self.request.GET.get('do_filter')) if self.request.GET.get(
            'do_filter') else self.do_filter

        return super(MonitorWaterfall, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        date_from = self.kwargs['date_from']
        date_to = self.kwargs['date_to']

        q = models.DataAngin.objects.filter(
            tanggal__gte=date_from,
            tanggal__lte=date_to
        )

        return q

    def get(self, request, *args, **kwargs):
        obj = self.do_task()

        return HttpResponse(json.dumps([obj], sort_keys=True), content_type='Applications/json')

    def do_task(self):
        v_range = numpy.arange(0.0, self.vmax, self.step).tolist()
        obj = {}
        data_x = []
        data_y = []
        data_z = []

        for i, v in enumerate(v_range):
            v = round(v, 1)

            if self.arah == 'BR':
                data_acc = self.get_queryset().filter(
                    waktu__gte=self.wkt_awl,
                    waktu__lte=self.wkt_akh,
                    kecepatan__gte=v,
                    kecepatan__lt=v + self.step,
                    arah__gte=225.0,
                    arah__lte=315.0
                ).values_list(
                    'akselerator1', 'akselerator2', 'akselerator3', 'akselerator4', 'akselerator5'
                )

            else:
                data_acc = self.get_queryset().filter(
                    waktu__gte=self.wkt_awl,
                    waktu__lte=self.wkt_akh,
                    kecepatan__gte=v,
                    kecepatan__lt=v + self.step,
                    arah__gte=45.0,
                    arah__lte=135.0
                ).values_list(
                    'akselerator1', 'akselerator2', 'akselerator3', 'akselerator4', 'akselerator5'
                )

            # Data akselerometer
            numpy_data_acc = numpy.array(data_acc).flatten()

            # Jumlah data
            N = numpy_data_acc.size

            # Sample spacing
            T = self.sample_spacing

            data_x.append([str(v)[:3]+' - '+str(v+self.step)[:3]] * N)
            if N > 0:
                # FFT
                fltr = DoFilter(data=numpy_data_acc).butter_bandpass_filter(self.first_cutoff,
                                                                            self.second_cutoff,
                                                                            1 / T,
                                                                            order=self.order)
                zf = numpy.fft.fft(fltr)
                m = numpy.absolute(zf[:N // 2])
                yf = numpy.fft.fftfreq(N, d=T).tolist()

                data_y.append(yf[:N // 2])
                data_z.append(m.tolist())

            else:
                data_y.append(0.0)
                data_z.append(0.0)

        obj['x'] = data_x
        obj['y'] = data_y
        obj['z'] = data_z

        return obj
