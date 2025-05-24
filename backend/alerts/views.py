from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets, permissions
from .models import PriceAlert
from .serializers import PriceAlertSerializer


class PriceAlertViewSet(viewsets.ModelViewSet):
    serializer_class = PriceAlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PriceAlert.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)