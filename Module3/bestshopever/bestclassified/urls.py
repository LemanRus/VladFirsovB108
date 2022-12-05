from .views import index, about

from django.urls import path, re_path

urlpatterns = [
    path('ok/', index, name='index'),
    re_path(r'^about/$', about, name='about')
]

