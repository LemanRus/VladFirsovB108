from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import DetailView


# Create your views here.


class LogoutView(View):
    pass


class SignUpView(View):
    pass


class ProfileView(DetailView):
    pass


class ProfileEditView(View):
    pass