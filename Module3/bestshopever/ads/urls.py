from .views import index, recent_ads, ad_show, ad_edit, ad_create, ad_delete, rate_ad

from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^ads/(?P<ad_id>\w+)$', ad_show, name='ad_show'),
    path('ads/recent/', recent_ads, name='recent_ads'),
    path('ads/create/', ad_create, name='ad_create'),
    path('ads/<int:ad_id>/delete/', ad_delete, name='ad_delete'),
    path('ads/<int:ad_id>/edit/', ad_edit, name='ad_edit'),
    path('ads/<int:ad_id>/rate/', rate_ad, name='rate_ad'),
]

