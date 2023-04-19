from django.urls import path

from bookings.views import BookingForm, MyBookings, BookingDetailsPage, CancelBooking

urlpatterns = [
    path('<int:pk>/', BookingForm.as_view(), name='BookingForm'),
    path('BookingDetailsPage/<int:pk>/', BookingDetailsPage.as_view(), name='BookingDetailsPage'),
    path('MyBookings/', MyBookings.as_view(), name='MyBookings'),
    path('CancelBooking/<int:pk>/', CancelBooking.as_view(), name='CancelBooking')
]
