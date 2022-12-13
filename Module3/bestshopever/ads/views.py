import time

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from . import models
from .forms import AdCreateForm
from .models import Advertisement, Category
from bestclassified.models import Rating


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
    template_name = 'ads/ad_create.html'
    if request.method == 'GET':
        form = AdCreateForm()
        context = {'form': form,}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = AdCreateForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.date_pub = timezone.now()
            ad.save()
            return redirect(reverse('ads:ad_show', kwargs={'ad_id': ad.id}))
        else:
            context = {'form': form}
            return render(request, template_name, context)


def ad_edit(request, ad_id):
    return HttpResponse("Edit ad")


def ad_delete(request, ad_id):
    return HttpResponse("Delete ad")


def rate_ad_author(request, ad_id):
    ad = get_object_or_404(models.Advertisement, pk=ad_id)
    if request.user and request.user.is_authenticated:
        ad_rating, created = Rating.objects.get_or_create(user_who_rate=request.user, user_rated=ad.author)
        ad_rating.rating_value = request.POST.get('selected_rating')
        ad_rating.save()
    return redirect(request.META.get('HTTP_REFERER'), request)

