from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from application.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .serializers import enquiry_tableSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.contrib.auth.models import User 
from .forms import ContactForm
import logging





def home(request):
    return render(request, 'index.html')
def servicedetails(request):
    return render(request, 'servicedetails.html')
def servicedetails2(request):
    return render(request, 'servicedetails2.html')
def servicedetails3(request):
    return render(request, 'servicedetails3.html')
def servicedetails4(request):
    return render(request, 'servicedetails4.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def properties(request):
    return render(request, 'properties.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    return render(request, 'contact.html')


def index(request):
    # Render the index page with the login popup
    return render(request, 'index.html')

@login_required
def home(request):
    # Render the home page, accessible only when logged in
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')  # Show error message
            return redirect('index')  # Redirect back to index page if authentication fails

    else:  # Handle GET request by rendering the login form (index.html)
        return render(request, 'index.html')  # Render the login page (index.html)
    
def profile(request):
    # Render the profile page
    return render(request, 'profile.html')  # Ensure you have a profile.html template
    
def logout_view(request):
    logout(request)  # Clears session and authentication
    request.session.flush()  # Clears all session data
    return redirect('index')  # Redirect to homepage



@login_required
def profile(request):
    if request.method == 'POST':
        # Update user information
        full_name = request.POST.get('full_name').split()
        if len(full_name) > 1:
            request.user.first_name = full_name[0]
            request.user.last_name = full_name[1]
        request.user.save()

        # Update profile information
        mobile_number = request.POST.get('mobile_number')
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.mobile_number = mobile_number
        profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  # Redirect to the profile page after update

    return render(request, 'profile.html')  # Render the profile page

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('index')  # Redirect instead of render

        # Check if username is taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('index')

        # Check if email is taken
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('index')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = full_name
        user.save()

        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')  # Or wherever appropriate

        return redirect('index')  # Fallback if not POST
        
        
        
        
        

        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = full_name
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            print("User  created successfully message set.")
            return redirect('login')  # Make sure 'login' URL exists
        except Exception as e:
            messages.error(request, f'Error creating account: {e}')
            print(f'Exception: {e}')  # Log exception for debugging

    # If GET or errors, render signup page again
    return render(request, 'index.html')

def validate_field(request):
    field = request.GET.get('field')
    value = request.GET.get('value')

    response = {}

    if field == 'username' and User.objects.filter(username=value).exists():
        response['message'] = 'Username is already taken.'
    elif field == 'email' and User.objects.filter(email=value).exists():
        response['message'] = 'Email is already registered.'

    return JsonResponse(response)

def some_view(request):
    # Redirect to the index page and show the login popup
    return redirect('/index/?show_login=true')

def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # logic for sending the email (or handling the form submission)
            
            sent = True  # Set sent to True when the form is valid and successfully submitted

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'sent': sent})

def contact_view(request):
    sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sent = True
            form = ContactForm()  # Resets form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'sent': sent})

def ev_charging_page(request):
    return render(request, 'ev_charging.html')

def ev_charging_page2(request):
    return render(request, 'ev_charging2.html')


def get_nearby_charging_stations(request):
    # Get latitude and longitude from the request parameters
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    distance = request.GET.get('distance', 1000)  # Default distance is 1000 km if not provided

    # If lat or lng is missing, return an error
    if not lat or not lng:
        return JsonResponse({'error': 'Missing latitude or longitude'}, status=400)

    # OpenChargeMap API URL
    url = "https://api.openchargemap.io/v3/poi/"
    params = {
        'output': 'json',
        'countrycode': 'IN',  # India
        'latitude': lat,
        'longitude': lng,
        'maxresults': 50,  # Return up to 50 results
        'distance': distance,  # Use the provided distance or default to 1000 km
        'distanceunit': 'KM',
        'compact': 'true',
        'verbose': 'false',
        'key': '2733d667-aab6-49b1-8751-4b659e71fc4c'  # OpenChargeMap API key
    }

    # Fetch data from OpenChargeMap API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)
    

def get_random_charging_stations(request):
    # Default coordinates (center of India)
    lat = 21.1458  # Default latitude (central India)
    lng = 79.0882  # Default longitude (central India)
    distance = request.GET.get('distance', 1000)  # Default distance is 1000 km if not provided

    # OpenChargeMap API URL
    url = "https://api.openchargemap.io/v3/poi/"
    params = {
        'output': 'json',
        'countrycode': 'IN',  # India
        'latitude': lat,
        'longitude': lng,
        'maxresults': 50,  # Return up to 50 results
        'distance': distance,  # Use the provided distance or default to 1000 km
        'distanceunit': 'KM',
        'compact': 'true',
        'verbose': 'false',
        'key': '2733d667-aab6-49b1-8751-4b659e71fc4c'  # OpenChargeMap API key
    }

    # Fetch data from OpenChargeMap API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)
    

def battery_swap_stations(request):
    # This view renders the page for battery swap stations
    return render(request, 'battery_swap.html')  # Make sure the name is 'battery_swap.html'

def get_battery_swap_stations(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    if not lat or not lng:
        return JsonResponse({'error': 'Missing latitude or longitude'}, status=400)

    url = "https://api.openchargemap.io/v3/poi/"
    params = {
        'output': 'json',
        'countrycode': 'IN',
        'maxresults': 50,
        'distance': 1000,  # Wide radius to capture more results
        'distanceunit': 'KM',
        'compact': 'true',
        'verbose': 'false',
        'latitude': lat,
        'longitude': lng,
        'key': '2733d667-aab6-49b1-8751-4b659e71fc4c'  
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

           
            swap_stations = [
                {
                    'name': station['AddressInfo'].get('Title'),
                    'address': station['AddressInfo'].get('AddressLine1'),
                    'latitude': station['AddressInfo'].get('Latitude'),
                    'longitude': station['AddressInfo'].get('Longitude')
                }
                for station in data
                if 'Battery' in str(station.get('UsageType', {}).get('Title', '')).lower() or
                   'swap' in str(station.get('UsageType', {}).get('Title', '')).lower()
            ]

            return JsonResponse(swap_stations, safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch stations'}, status=500)
    except Exception as e:
        print("API ERROR:", e)
        return JsonResponse({'error': 'Server error occurred'}, status=500)