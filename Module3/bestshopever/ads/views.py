from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from . import models
from .models import Advertisement, Category


def index(request):
    ad_query = Advertisement.objects.order_by('-date_pub')[:7]
    context = {
        'ads': ad_query
    }
    return render(request, 'ads/index.html', context)


def recent_ads(request):
    ad_query = Advertisement.objects.order_by('-date_pub')
    context = {
        'ads': ad_query
    }
    return render(request, 'ads/recent_ads.html', context)


def categories(request):
    categories_query = Category.objects.all()
    context = {
        'categories': categories_query
    }
    return render(request, 'ads/categories.html', context)


def category_show(request, category_id):
    category = get_object_or_404(models.Category, pk=category_id)
    context = {
        'category': category,
    }
    return render(request, 'ads/category_show.html', context)


def ad_show(request, ad_id):
    ad = get_object_or_404(models.Advertisement, pk=ad_id)
    context = {
        'ad': ad,
    }
    return render(request, 'ads/ad_show.html', context)


def ad_create(request):
    return HttpResponse("New ad")


def ad_edit(request, ad_id):
    return HttpResponse("Edit ad")


def ad_delete(request, ad_id):
    return HttpResponse("Delete ad")


def rate_ad(request, ad_id):
    return HttpResponse("Rate ad")

