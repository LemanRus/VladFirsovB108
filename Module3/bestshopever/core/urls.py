from django.urls import path, re_path, reverse
from django.views.generic import TemplateView

from . import views
from .models import CustomUser

app_name = 'core'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_completed/', TemplateView.as_view(template_name='core/password_reset_complete.html'),
         name="password_reset_completed"),
    path('<int:user_id>/', views.ProfileView.as_view(), name="profile"),
    path('<int:user_id>/edit/', views.ProfileEditView.as_view(), name="profile_edit"),
    path('<int:profile_id>/rate/', views.rate_user, name='rate_user'),
]
