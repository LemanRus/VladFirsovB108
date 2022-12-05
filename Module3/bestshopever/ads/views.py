from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Best shop ever")


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

