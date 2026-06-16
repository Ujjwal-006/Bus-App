from django.contrib import admin
from .models import Booking, wallet, alerts

admin.site.register(Booking)
admin.site.register(wallet)
admin.site.register(alerts)