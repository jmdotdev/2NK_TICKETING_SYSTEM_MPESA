from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from core.models import Route


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    Time = models.TimeField(auto_now_add=False)
    persons = models.PositiveIntegerField(default=0)
    mobile_no = models.CharField(max_length=15)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.route.From + str(self.route.Destination)

    class Meta:
        verbose_name_plural = 'Bookings'

