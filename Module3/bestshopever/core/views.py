from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from core.models import CustomUser
from .forms import SignupForm


# Create your views here.


def logout_view(request):
    logout(request)
    return redirect(reverse("ads:index"))


class SignUpView(View):
    template_name = 'core/signup.html'
    form = SignupForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('core:profile', kwargs={'user_id': user.id}))
        else:
            return render(request, self.template_name, {
                'form': form,
            })


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'core/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'


class ProfileEditView(View):
    pass