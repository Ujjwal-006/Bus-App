from django.contrib import admin
from .models import Booking, wallet, alerts, Profile

admin.site.register(Booking)
admin.site.register(wallet)
admin.site.register(alerts)
admin.site.register(Profile)

