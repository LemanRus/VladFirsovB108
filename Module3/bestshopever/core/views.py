from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, UpdateView

from .models import CustomUser, Rating
from .forms import SignupForm, PasswordResetValidateForm


# Create your views here.


def logout_view(request):
    logout(request)
    return redirect(reverse("ads:index"))

# TODO: сделать форму на классе для отображения ошибки
def rate_user(request, profile_id):
    profile = get_object_or_404(CustomUser, pk=profile_id)
    if request.user and request.user.is_authenticated:
        profile_rating, created = Rating.objects.get_or_create(user_who_rate=request.user, user_rated=profile)
        profile_rating.rating_value = request.POST.get('selected_rating')
        profile_rating.save()
    return redirect(request.META.get('HTTP_REFERER'), request)


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


class ProfileEditView(UpdateView):
    model = CustomUser
    template_name = 'core/edit_profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'
    form_class = SignupForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != request.user:
            raise Http404('You are not allowed to edit profile that is not yours')
        return super().dispatch(request, *args, **kwargs)


class PasswordResetView(View):
    template_name = 'core/password_reset.html'
    context = {
        'error': "",
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        email_for_reset = request.POST.get('email_for_reset')
        if email_for_reset and not CustomUser.objects.filter(email=email_for_reset).exists():
            self.context['error'] = 'Email does not exist. Check it or sign up:'
            return render(request, self.template_name, self.context)
        else:
            user = CustomUser.objects.filter(email=email_for_reset).get()
            return redirect(reverse('core:password_reset_validate',  kwargs={'user_id': user.id}))


class PasswordResetValidateView(View):
    template_name = 'core/password_reset_validate.html'
    form = PasswordResetValidateForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form,
            'secret_question': CustomUser.objects.get(pk=kwargs['user_id']).secret_question,
            'user_id': kwargs['user_id'],
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        user_who_reset = CustomUser.objects.get(pk=kwargs['user_id'])
        if form.data.get('secret_answer') != user_who_reset.secret_answer:
            form.add_error('secret_answer', 'Secret answer is not correct')
        if form.is_valid():
            print(user_who_reset)
            user_who_reset.password = form.cleaned_data.get('password')
            user_who_reset.save()
            return redirect(reverse('core:password_reset_completed'))
        else:
            return render(request, self.template_name, {
                'form': form,
                'secret_question': user_who_reset.secret_question,
                'user_id': kwargs['user_id'],
            })