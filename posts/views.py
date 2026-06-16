from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
import random
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Booking
from .models import Profile
from .models import alerts
# Create your views here.
def login_page(request):
    if request.method == 'POST':

        username_input = request.POST.get('username')
        passward_input = request.POST.get('passward')

        user  = authenticate(request, username=username_input, password=passward_input)
    
        if user is not None:
            login(request, user)
            return redirect('shader_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
        
    return render(request, 'login.html')


@login_required(login_url='transit:login_user')
def booking_page(request):

    all_user_tickets = Booking.objects.filter(user=request.user)  
    
    upcoming_trips = all_user_tickets.filter(status='Upcoming').order_by('date', 'time')
    past_trips = all_user_tickets.exclude(status='Upcoming').order_by('-date')
    
    context = {
        'upcoming_trips': upcoming_trips,
        'past_trips': past_trips,
    }
    return render(request, 'booking.html', context)


def alert_page(request):

    all_alerts = alerts.objects.all().order_by('-id')
    
    context = {
        'alerts': all_alerts
    }
    return render(request, 'alert.html', context)

def wallet_page(request):
    return render(request, 'wallet.html')

def accontsetting_page(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Grab the newly typed data from the form
        profile.full_name = request.POST.get('full_name')
        profile.phone = request.POST.get('phone')
        profile.timezone = request.POST.get('timezone')
        profile.save() 

        new_email = request.POST.get('email')
        if new_email:
            request.user.username = new_email
            request.user.email = new_email
            request.user.save()

        return redirect('accont_settings')

    # 3. If they are just opening the page normally, load the layout and pass the profile data
    context = {
        'profile': profile
    }
    return render(request, 'accontsetting.html', context)

def shader_page(request):
    if request.method == 'POST':
        dep_station = request.POST.get('departure')
        dest_station = request.POST.get('destination')
        journey_date = request.POST.get('journey_date')

        if dep_station  and dest_station:

            ticket_ref = f"TJ-{random.randint(10000, 99999)}"

            exact_time = datetime.now().strftime("%H:%M:%S")

            car_num = random.choice(1, 8)
            seat_num = random.choice(1, 40)
            seat_letter = random.choice(['A', 'B', 'C', 'D'])
            assigned_seat = f"Car 0{car_num}, Seat {seat_num}{seat_letter}"
        

            booking_page.object.create(
                user=request.user,
                Reference=ticket_ref,
                route_from=dep_station,
                route_to=dest_station,
                date=journey_date,
                time=exact_time,
                seat=assigned_seat,
                status='Upcomeing'
            )

            return redirect('my_bookings')
        
    return render(request, 'shader.html')

