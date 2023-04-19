from django.urls import path

from core.views import *
urlpatterns = [
    path('', HomePage.as_view(), name="HomePage"),
    path('AboutUs/', AboutUs.as_view(), name="AboutUs"),
    path('Routes/', Routes.as_view(), name="Routes"),
    path('RoutesDetail/<int:pk>/', RoutesDetail.as_view(), name="RoutesDetail"),
    path('AddRoute', AddRoute.as_view(), name="AddRoute"),
    path('Update_Route/<int:pk>/', Update_Route.as_view(), name="Update_Route"),
    path('Cars/', Cars.as_view(), name="Cars"),
    path('AddCar/', AddCar.as_view(), name="AddCar"),
    path('UpdateCar/<int:pk>/', UpdateCar.as_view(), name="UpdateCar"),
    path('CarDetail/<int:pk>/', CarDetail.as_view(), name="CarDetail"),
    path('AddBooking/', AddBooking.as_view(), name="AddBooking"),
    path('ContactUs/', ContactUs.as_view(), name="ContactUs"),
    path('AddTestimonials/', AddTestimonials.as_view(), name="AddTestimonials"),
    path('AdminPage/', AdminPage.as_view(), name="AdminPage"),
    path('AdminManageBookings/<int:pk>/', AdminManageBookings.as_view(), name="AdminManageBookings"),
    path('Search/', Search.as_view(), name="Search"),
    path('DeleteRoute/<int:pk>/', DeleteRoute.as_view(), name="DeleteRoute"),
    path('DeleteCar/<int:pk>/', DeleteCar.as_view(), name="DeleteCar"),
    path('DeleteBooking/<int:pk>/', DeleteBooking.as_view(), name="DeleteBooking"),
]
