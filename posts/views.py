from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import random
import csv
import os
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Booking
from .models import Profile
from .models import alerts
from .models import wallet

# ── Load all cities from the CSV file ──────────────────────────────────────────
def get_cities():
    cities = []
    # Path: project_root/city.csv/cities_r2.csv
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'city.csv', 'cities_r2.csv')
    try:
        # utf-8-sig strips the BOM character that Excel adds to CSV files.
        # Without this, the first column 'City' becomes '\ufeffCity' and nothing matches.
        with open(csv_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Try 'name_of_city' or 'City' column; strip whitespace to handle sloppy headers
                name = (row.get('name_of_city') or row.get('City') or row.get(' City') or '').strip()
                if name:
                    cities.append(name)
    except FileNotFoundError:
        # Fallback list — site still works if CSV is missing
        cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
                  "Kolkata", "Pune", "Jaipur", "Surat", "Lucknow"]
    return cities


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        user = authenticate(request, username=username_input, password=password_input)
        if user is not None:
            login(request, user)
            return redirect('transit:schedules')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('transit:schedules')


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

@login_required(login_url='transit:login_user')
def cancel_booking(request, reference):
    if request.method == 'POST':
        # Find the booking belonging to the user with the given reference
        booking = Booking.objects.filter(user=request.user, reference=reference).first()
        if booking:
            booking.status = 'Cancelled'
            booking.save()
            messages.success(request, f"Booking {reference} has been cancelled.")
    return redirect('transit:my_bookings')


@login_required(login_url='transit:login_user')
def alert_page(request):
    all_alerts = alerts.objects.all().order_by('-id')
    context = {'alerts': all_alerts}
    return render(request, 'alert.html', context)


@login_required(login_url='transit:login_user')
def wallet_page(request):
    user_wallet, created = wallet.objects.get_or_create(user=request.user)
    context = {'wallet': user_wallet}
    return render(request, 'wallet.html', context)


@login_required(login_url='transit:login_user')
def accontsetting_page(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.phone = request.POST.get('phone')
        profile.timezone = request.POST.get('timezone')
        profile.save()
        new_email = request.POST.get('email')
        if new_email:
            request.user.username = new_email
            request.user.email = new_email
            request.user.save()
        return redirect('transit:account_settings')
    context = {'profile': profile}
    return render(request, 'accontsetting.html', context)


@login_required(login_url='transit:login_user')
def shader_page(request):
    # ── Load all Indian cities from CSV for the autocomplete search bar ──
    cities_json = json.dumps(get_cities())

    if request.method == 'POST':
        dep_station  = request.POST.get('departure', '').strip()
        dest_station = request.POST.get('destination', '').strip()
        journey_date = request.POST.get('journey_date', '').strip()

        if dep_station and dest_station and journey_date:
            # Store route data in session, then go to seat selection
            request.session['pending_booking'] = {
                'departure':    dep_station,
                'destination':  dest_station,
                'journey_date': journey_date,
            }
            return redirect('transit:seat_selection')

    return render(request, 'shader.html', {'cities_json': cities_json})


@login_required(login_url='transit:login_user')
def seat_selection_page(request):
    """
    Shows the interactive bus seat map.
    Red seats = already booked for this route+date.
    User picks a seat → booking is saved.
    """
    pending = request.session.get('pending_booking')
    if not pending:
        # No booking data in session — send back to dashboard
        return redirect('transit:schedules')

    dep_station  = pending['departure']
    dest_station = pending['destination']
    journey_date = pending['journey_date']

    if request.method == 'POST':
        chosen_seat = request.POST.get('selected_seat', '').strip()
        if chosen_seat:
            ticket_ref = f"TJ-{random.randint(10000, 99999)}"
            exact_time = datetime.now().strftime("%H:%M:%S")
            Booking.objects.create(
                user=request.user,
                reference=ticket_ref,
                route_from=dep_station,
                route_to=dest_station,
                date=journey_date,
                time=exact_time,
                seat=chosen_seat,
                status='Upcoming'
            )
            # Clear session data after booking is saved
            del request.session['pending_booking']
            return redirect('transit:my_bookings')

    # Find which seats are already booked for this route + date
    booked_seats = list(
        Booking.objects.filter(
            route_from=dep_station,
            route_to=dest_station,
            date=journey_date
        ).values_list('seat', flat=True)
    )

    context = {
        'dep_station':  dep_station,
        'dest_station': dest_station,
        'journey_date': journey_date,
        'booked_seats': json.dumps(booked_seats),
    }
    return render(request, 'seat_selection.html', context)


@login_required(login_url='transit:login_user')
def payment_page(request):
    return render(request, 'Payment.html')


@login_required(login_url='transit:login_user')
def live_tracking_page(request):
    return render(request, 'live tracking.html')