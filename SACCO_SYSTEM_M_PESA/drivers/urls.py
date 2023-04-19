from django.urls import path

from drivers.views import DriversView, DeleteDriver,UpdateDriver

urlpatterns = [
    path('', DriversView.as_view(), name='DriversView'),
    path('DeleteDriver/<int:pk>/', DeleteDriver.as_view(), name='DeleteDriver'),
    path('UpdateDriver/<int:pk>/', UpdateDriver.as_view(), name='UpdateDriver'),
]
