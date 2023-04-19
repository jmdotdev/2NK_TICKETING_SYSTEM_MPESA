from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView, UpdateView

from core.forms import AddFriverForm
from drivers.models import Driver


class DriversView(FormView):
    template_name = 'Add_driver.html'
    form_class = AddFriverForm
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteDriver(DeleteView):
    template_name = 'delete.html'
    model = Driver
    success_url = '/'


class UpdateDriver(UpdateView):
    model = Driver
    template_name = 'UpdateDriver.html'
    fields = '__all__'
    success_url = '/'
