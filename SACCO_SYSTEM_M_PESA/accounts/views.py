from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from core.forms import RegisterUserForm


class RegisterUser(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'Register.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'account created successfully')
            return redirect('LoginPage')
        return render(request, 'Register.html', {'form': form})


class LoginPage(LoginView):
    template_name = 'LoginPage.html'


class AdminLogin(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        return redirect('AdminPage')

    def post(self, request):
        return redirect('AdminPage')


class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
