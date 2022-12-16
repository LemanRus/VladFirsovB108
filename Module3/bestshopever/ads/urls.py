from django.views.generic import TemplateView

from . import views

from django.urls import path, re_path

app_name = 'ads'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('ads/recent/', views.AdList.as_view(), name='recent_ads'),
    path('ads/create/', views.AdCreate.as_view(), name='ad_create'),
    path('ads/<int:ad_id>/delete/', views.AdDelete.as_view(), name='ad_delete'),
    path('ads/<int:ad_id>/ad-delete-success/', TemplateView.as_view(template_name='ads/ad_delete_success.html'), name='ad-delete-success'),
    path('ads/<int:ad_id>/edit/', views.AdEdit.as_view(), name='ad_edit'),
    path('ads/<int:ad_id>/rate/', views.rate_ad_author, name='rate_ad_author'),
    re_path(r'^ads/(?P<ad_id>\w+)$', views.AdDetailed.as_view(), name='ad_show'),
    re_path(r'^(?P<category_id>\w+)$', views.CategoryDetailed.as_view(), name='category_show'),
]

