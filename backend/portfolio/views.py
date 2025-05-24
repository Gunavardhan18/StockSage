from rest_framework import viewsets
from .models import Portfolio, StockHolding
from .serializers import PortfolioSerializer, StockHoldingSerializer
from rest_framework.permissions import IsAuthenticated

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StockHoldingViewSet(viewsets.ModelViewSet):
    serializer_class = StockHoldingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StockHolding.objects.filter(portfolio__user=self.request.user)
