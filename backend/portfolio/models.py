from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class StockHolding(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='holdings', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} ({self.quantity})"
