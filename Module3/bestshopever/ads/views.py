import time

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from . import models
from .forms import AdCreateForm
from .models import Advertisement, Category
from bestclassified.models import Rating


class IndexView(ListView):
    model = Advertisement
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    queryset = Advertisement.objects.order_by('-date_pub')[:7]



class AdList(ListView):
    model = Advertisement
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    queryset = Advertisement.objects.order_by('-date_pub')


class Categories(ListView):
    model = Category
    template_name = 'ads/categories.html'
    context_object_name = 'categories'


class CategoryDetailed(DetailView):
    model = Category
    template_name = 'ads/category_show.html'
    context_object_name = 'category'


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

