from django.urls import path, re_path, reverse
from . import views
from .models import CustomUser

app_name = 'core'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('<int:user_id>/', views.ProfileView.as_view(), name="profile"),
    path('<int:user_id>/edit/', views.ProfileEditView.as_view(), name="profile_edit"),
]

