"""Project6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views
from django.urls import path
from .views import index, home, login_view
from django.urls import path
from .views import signup
from .views import index, home, services, properties, agents, contact, profile, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # homepage with login popup
    path('home/', home, name='home'),  # logged-in homepage
    path('login/', login_view, name='login'),  # login POST handler
    path('signup/', signup, name='signup'),
    path('validate/', views.validate_field, name='validate_field'),
    path('contact/', views.contact_view, name='contact' ),
    path('servicedetails/', views.servicedetails, name='servicedetails' ),
    path('servicedetails2/', views.servicedetails2, name='servicedetails2' ),
    path('servicedetails3/', views.servicedetails3, name='servicedetails3' ),
    path('servicedetails4/', views.servicedetails4, name='servicedetails4' ),
    path('about/', views.about, name='about' ),
    path('services/', views.services, name='services' ),
    path('properties/', views.properties, name='properties' ),
    path('agents/', views.agents, name='agents' ),
    path('contact/', views.contact, name='contact' ),
    path('profile/', views.profile, name='profile'),  # Add this view
    path('logout/', views.logout_view, name='logout'),  # Add this view
    path('ev-charging/', views.ev_charging_page, name='ev_charging'),
    path('ev-charging2/', views.ev_charging_page2, name='ev_charging2'),
    path('battery-swap/', views.battery_swap_stations, name='battery_swap'),
    path('get-battery-swap-stations/', views.get_battery_swap_stations, name='battery_swap_stations'),
    path('get-nearby-charging-stations/', views.get_nearby_charging_stations, name='get_nearby_charging_stations'),
    path('get-random-charging-stations/', views.get_random_charging_stations, name='get_random_charging_stations'),

    
]