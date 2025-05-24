from rest_framework import serializers
from .models import Portfolio, StockHolding

class StockHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHolding
        fields = '__all__'
        read_only_fields = ['portfolio']

class PortfolioSerializer(serializers.ModelSerializer):
    holdings = StockHoldingSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'holdings']
