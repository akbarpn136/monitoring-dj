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
