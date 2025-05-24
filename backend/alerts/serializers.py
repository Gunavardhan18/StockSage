# alerts/serializers.py
from rest_framework import serializers
from .models import PriceAlert

class PriceAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAlert
        fields = '__all__'
        read_only_fields = ['user', 'triggered']