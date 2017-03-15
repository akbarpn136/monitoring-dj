from rest_framework import serializers
from monitoring import models


class MonitorAnginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataAngin
        fields = '__all__'
