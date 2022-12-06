from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Advertisement


def index(request):
    ad_query = Advertisement.objects.order_by('-date_pub')[:10]
    output = [f"{ad.title} from {ad.author} published: {ad.date_pub}\n" for ad in ad_query]
    template = loader.get_template('ads/index.html')
    context = {
        'ads': ad_query
    }
    return HttpResponse(template.render(context))


def recent_ads(request):
    return HttpResponse("Recent ads")


def category_show(request, categoty_id):
    return HttpResponse("Category")


def ad_show(request, ad_id):
    return HttpResponse("Ad")


def ad_create(request):
    return HttpResponse("New ad")


def ad_edit(request, ad_id):
    return HttpResponse("Edit ad")


def ad_delete(request, ad_id):
    return HttpResponse("Delete ad")


def rate_ad(request, ad_id):
    return HttpResponse("Rate ad")

