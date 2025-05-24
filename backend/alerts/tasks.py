# alerts/tasks.py
from celery import shared_task
from .models import PriceAlert
import requests

def fetch_current_price(symbol):
    # Dummy logic - replace with real stock API call
    return 100.0

@shared_task
def check_price_alert(alert_id):
    try:
        alert = PriceAlert.objects.get(id=alert_id, triggered=False)
        current_price = fetch_current_price(alert.symbol)

        if (alert.direction == 'above' and current_price > alert.target_price) or \
           (alert.direction == 'below' and current_price < alert.target_price):
            alert.triggered = True
            alert.save()
            print(f"ALERT TRIGGERED for {alert.symbol} at {current_price}")
        else:
            print(f"No trigger: {alert.symbol} at {current_price}")

    except PriceAlert.DoesNotExist:
        pass

@shared_task
def check_all_alerts():
    alerts = PriceAlert.objects.filter(triggered=False)
    for alert in alerts:
        check_price_alert.delay(alert.id)