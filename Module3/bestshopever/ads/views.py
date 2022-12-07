from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from . import models
from .models import Advertisement


def index(request):
    ad_query = Advertisement.objects.order_by('-date_pub')[:10]
    context = {
        'ads': ad_query
    }
    return render(request, 'ads/index.html', context)


def recent_ads(request):
    return HttpResponse("Recent ads")


def category_show(request, categoty_id):
    return HttpResponse("Category")


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

