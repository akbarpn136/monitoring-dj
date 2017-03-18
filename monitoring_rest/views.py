import json

import numpy
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import generics

from monitoring import models
from . import serializers


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

            data_x.append(str(v) + ' - ' + str(v+step))
            data_y.append(numpy_data_acc_root)

        obj['x'] = data_x
        obj['y'] = data_y

        return obj
