import time

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from . import models
from .forms import AdCreateForm
from .models import Advertisement, Category
from core.models import Rating


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
    pk_url_kwarg = 'category_id'


class AdDetailed(DetailView):
    model = Advertisement
    template_name = 'ads/ad_show.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'ad_id'


class AdCreate(CreateView):
    form_class = AdCreateForm
    template_name = 'ads/ad_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.date_pub = timezone.now()
            ad.save()
            context['form'] = self.form_class
            return redirect(reverse('ads:ad_show', kwargs={'ad_id': ad.id}))
        else:
            context['form'] = self.form_class
            return render(request, self.template_name, context)


class AdEdit(UpdateView):
    model = Advertisement
    template_name = 'ads/ad_edit.html'
    pk_url_kwarg = 'ad_id'
    form_class = AdCreateForm
    context_object_name = 'ad'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Exception('You are not allowed to edit! Go away!')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        ad_id = self.kwargs['ad_id']
        return reverse('ads:ad_show', args=(ad_id, ))


class AdDelete(DeleteView):
    model = Advertisement
    template_name = 'ads/ad_delete.html'
    pk_url_kwarg = 'ad_id'
    context_object_name = 'ad'

    def get_success_url(self):
        ad_id = self.kwargs['ad_id']
        return reverse('ads:ad-delete-success', args=(ad_id, ))


def rate_ad_author(request, ad_id):
    ad = get_object_or_404(models.Advertisement, pk=ad_id)
    if request.user and request.user.is_authenticated:
        ad_rating, created = Rating.objects.get_or_create(user_who_rate=request.user, user_rated=ad.author)
        ad_rating.rating_value = request.POST.get('selected_rating')
        ad_rating.save()
    return redirect(request.META.get('HTTP_REFERER'), request)

