from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, StockHoldingViewSet

router = DefaultRouter()
router.register('portfolios', PortfolioViewSet, basename='portfolio')
router.register('holdings', StockHoldingViewSet, basename='holding')

urlpatterns = [
    path('', include(router.urls)),
]
