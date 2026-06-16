from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1. USER PROFILE TABLE (Stores phone numbers, timezones, and wallet money)
class Profile(models.Model):
    # Links this profile directly to a unique Django User account
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Stores the user's full name (Defaults to "New User" if empty)
    full_name = models.CharField(max_length=100, default="New User")
    
    # Stores phone numbers. blank/null=True means this field is optional
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Stores selected timezone for transit schedules
    timezone = models.CharField(max_length=50, default="GMT +05:00 Eastern Time")
    
    # Stores wallet credits. max_digits=10 means numbers up to 99,999,999.99
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.user.username


# 2. BOOKINGS TABLE (Stores tickets bought by users)
class Booking(models.Model):
    # Dropdown options for the ticket status
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    # Links the ticket to the User who bought it. If user is deleted, delete their tickets too.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Ticket reference number (e.g., TJ-99201). Must be unique.
    reference = models.CharField(max_length=20, unique=True)
    
    # Departure city input field
    route_from = models.CharField(max_length=100)
    
    # Destination city input field
    route_to = models.CharField(max_length=100)
    
    # Date of journey
    date = models.DateField()
    
    # Time of departure
    time = models.TimeField()
    
    # Seat tracking string (e.g., "Car 04, Seat 12A")
    seat = models.CharField(max_length=20)
    
    # Status dropdown selector using the choices array from above
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming')

    def __str__(self):
        return f"{self.reference} | {self.route_from} - {self.route_to}"


# 3. SYSTEM ALERTS TABLE (Stores notifications shown on alert.html)
class alerts(models.Model):
    ALERT_TYPES = [
        ('warning', 'Warning'),
        ('check_circle', 'Confirmation'),
        ('schedule', 'Reminder'),
        ('update', 'Optimization')
    ]
    
    # Title of the notification
    title = models.CharField(max_length=200)
    
    # The main text message body of the notification
    message = models.TextField()
    
    # String representation of time (e.g., "12:45 PM • TODAY")
    timestamp = models.CharField(max_length=50)
    
    # Category icon flag matching your Tailwind templates
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    
    # Optional label tags (e.g., "T-72 LINE")
    line_tag = models.CharField(max_length=50, blank=True, null=True)
    
    # Tracks if the user clicked "Mark all as read"
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}  balance:{self.balence}"
    