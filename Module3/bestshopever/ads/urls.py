from . import views

from django.urls import path, re_path

app_name = 'ads'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('ads/recent/', views.AdList.as_view(), name='recent_ads'),
    path('ads/create/', views.ad_create, name='ad_create'),
    path('ads/<int:ad_id>/delete/', views.ad_delete, name='ad_delete'),
    path('ads/<int:ad_id>/edit/', views.ad_edit, name='ad_edit'),
    path('ads/<int:ad_id>/rate/', views.rate_ad_author, name='rate_ad_author'),
    re_path(r'^ads/(?P<ad_id>\w+)$', views.ad_show, name='ad_show'),
    re_path(r'^(?P<category_id>\w+)$', views.CategoryDetailed.as_view(), name='category_show'),
]

