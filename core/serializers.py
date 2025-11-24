from rest_framework import serializers
from .models import MetricaSeguranca

class MetricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricaSeguranca
        fields = '__all__'