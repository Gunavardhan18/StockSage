from django.db import models
from django.contrib.auth.models import User

class PriceAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    target_price = models.FloatField()
    direction = models.CharField(max_length=5, choices=(('above', 'Above'), ('below', 'Below')))
    triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.symbol} {self.direction} {self.target_price}"
