# alerts/admin.py
from django.contrib import admin
from .models import PriceAlert

admin.site.register(PriceAlert)