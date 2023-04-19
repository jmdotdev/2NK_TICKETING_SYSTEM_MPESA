from django.contrib import admin

# Register your models here.
from bookings.models import Booking

admin.site.register(Booking)