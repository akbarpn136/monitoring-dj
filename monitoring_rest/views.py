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
            obj = {}

        return HttpResponse(json.dumps(obj, sort_keys=True), content_type='Applications/json')
