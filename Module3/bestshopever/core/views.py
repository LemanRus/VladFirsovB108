from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from core.models import CustomUser


# Create your views here.


def logout_view(request):
    logout(request)
    return redirect(reverse("posts:index"))


class SignUpView(View):
    pass


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'core/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'


class ProfileEditView(View):
    pass