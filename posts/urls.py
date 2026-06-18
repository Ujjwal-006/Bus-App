from django.urls import path
from . import views

# This must match the namespace we defined in Step 1
app_name = 'transit'

urlpatterns = [
    # 1. Homepage (shader.html)
    path('', views.shader_page, name='schedules'),
    
    # 2. Login Page (login.html)
    path('login/', views.login_page, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    
    # 3. Booking Page (booking.html)
    path('booking/', views.booking_page, name='my_bookings'),
    
    # 4. Alerts Page (alert.html)
    path('alerts/', views.alert_page, name='alerts'),
    
    # 5. Wallet Page (wallet.html)
    path('wallet/', views.wallet_page, name='wallet'),
    
    # 6. Settings Page (accont setting.html)
    path('accountsetting/', views.accontsetting_page, name='account_settings'),

    path('payment/', views.payment_page, name='payment'),

    path('tracking/', views.live_tracking_page, name='live_tracking'),

    # 7. Seat Selection Page
    path('seats/', views.seat_selection_page, name='seat_selection'),

]