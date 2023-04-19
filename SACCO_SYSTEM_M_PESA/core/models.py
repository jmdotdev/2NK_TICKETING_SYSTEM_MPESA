from django.contrib import messages
from django.db import models

Fuel_Choices = [
    ('petrol', 'petrol'),
    ('diesel', 'diesel'),
]

Transmission_Choices = [
    ('Auto', 'Auto'),
    ('Manual', 'Manual'),
]


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=300)
    capacity = models.PositiveIntegerField()
    plate_no = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100, choices=Fuel_Choices)
    Transmission = models.CharField(max_length=100, choices=Transmission_Choices)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cars'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def save_contacts(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

    class Meta:
        verbose_name_plural = 'Contacts'


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    avatar = models.ImageField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save_testimonial(self, request):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        avatar = request.FILES['avatar']
        message = request.POST.get('message')
        testimonial = Testimonial()
        testimonial.name = name
        testimonial.subject = subject
        testimonial.avatar = avatar
        testimonial.message = message
        testimonial.save()
        messages.info(request, 'testimonial added thankyou!!')
        return messages

    class Meta:
        verbose_name_plural = 'Testimonials'


class Route(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    From = models.CharField(max_length=200)
    Destination = models.CharField(max_length=200)
    Day = models.DateField(auto_now_add=False)
    Departure_Time = models.TimeField(auto_now_add=False)
    Arrival_time = models.TimeField(auto_now_add=False)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "From:" + str(self.From) + ":To:" + str(self.Destination)

    class Meta:
        verbose_name_plural = 'Routes'

    def get_time_to_reach_destination(self, pk):
        route = Route.objects.get(pk=pk)
        time_taken = route.Arrival_time - route.Departure_Time
        route.save()
        return time_taken


class Section_Counter(models.Model):
    years_experienced = models.PositiveIntegerField(default=0)
    total_cars = models.PositiveIntegerField(default=0)
    happy_customers = models.PositiveIntegerField(default=0)
    total_branches = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Section_Counter'
