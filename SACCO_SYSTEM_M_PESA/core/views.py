from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView, UpdateView, DeleteView

from bookings.models import Booking
from core.forms import AddCarForm, AddRouteForm, AddBookingForm
from core.models import Contact, Car, Testimonial, Route, Section_Counter
from drivers.models import Driver


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        context['counter'] = Section_Counter.objects.all()
        return context


class AboutUs(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['testimonial'] = Testimonial.objects.all()
        context['counter'] = Section_Counter.objects.all()
        return context

class Routes(TemplateView):
    template_name = 'Routes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route'] = Route.objects.all()
        return context


class RoutesDetail(DetailView):
    template_name = 'Routes_Detail.html'
    model = Route

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route'] = Route.objects.get(pk=self.kwargs.get('pk'))
        return context


class Cars(TemplateView):
    template_name = 'car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.all()
        return context


class CarDetail(DetailView):
    template_name = 'car-single.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetail, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(pk=self.kwargs.get('pk'))
        return context


class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        contacts = Contact()
        contacts.save_contacts(request=request)
        return render(request, 'contact.html')


class AddTestimonials(View):
    def get(self, request):
        return render(request, 'add_testimonial.html')

    def post(self, request):
        testimonial = Testimonial()
        testimonial.save_testimonial(request=request)
        return render(request, 'add_testimonial.html')


class AddCar(FormView):
    template_name = 'add_car.html'
    success_url = '/'
    form_class = AddCarForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


class UpdateCar(UpdateView):
    model = Car
    fields = ['name', 'image', 'capacity', 'fuel', 'plate_no', 'Transmission', 'description']
    template_name = 'update_car.html'
    success_url = '/'


class AddRoute(FormView):
    template_name = 'add_route.html'
    success_url = '/'
    form_class = AddRouteForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


class Update_Route(UpdateView):
    template_name = 'UpdateRoute.html'
    model = Route
    success_url = '/'
    fields = ['car', 'From', 'Destination', 'Day', 'Departure_Time', 'Arrival_time', 'price']


class AdminPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        elif request.user.is_authenticated and not request.user.is_superuser:
            return HttpResponse('Only Admins Can Access This Page!!')
        else:
            route = Route.objects.all()
            car = Car.objects.all()
            booking = Booking.objects.all()
            driver = Driver.objects.all()
            context = {'route': route, 'car': car, 'booking': booking, 'driver': driver}
            return render(request, 'AdminSite.html', context)

    def post(self, request):
        return render(request, 'AdminSite.html')


class Search(View):
    def get(self, request):
        fromt = request.GET.get('fromt')
        to = request.GET.get('to')
        date = request.GET.get('date')
        if fromt and to:
            route = Route.objects.all().filter(From__icontains=fromt, Destination__icontains=to).order_by('-id')
        elif fromt:
            route = Route.objects.all().filter(From__icontains=fromt).order_by('-id')
        elif to:
            route = Route.objects.all().filter(Destination__icontains=to).order_by('-id')
        elif date:
            route = Route.objects.all().filter(Day=date).order_by('-id')
        else:
            return render(request, 'Search.html')
        return render(request, 'Search.html', {'route': route})


class AdminManageBookings(UpdateView):
    template_name = 'update_details.html'
    model = Booking
    success_url = '/'
    fields = ['user', 'route', 'date', 'Time', 'persons', 'mobile_no', 'total']


class DeleteCar(DeleteView):
    model = Car
    template_name = 'delete.html'
    success_url = '/'


class DeleteRoute(DeleteView):
    model = Route
    template_name = 'delete.html'
    success_url = '/'


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete.html'
    success_url = '/'


class AddBooking(FormView):
    template_name = 'AddBooking.html'
    form_class = AddBookingForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
