import time

from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from . import models
from .forms import AdCreateForm, CommentForm
from .models import Advertisement, Category, Comment
from core.models import Rating


class IndexView(ListView):
    model = Advertisement
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    queryset = Advertisement.objects.order_by('-date_pub')[:4]


class AdList(ListView):
    model = Advertisement
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    queryset = Advertisement.objects.order_by('-date_pub')
    paginate_by = 12

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_listed'] = True
    #     return context


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
    comment_form = CommentForm
    template_name = 'ads/ad_show.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'ad_id'

    def get(self, request, ad_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['comments'] = Comment.objects.filter(ad__pk=ad_id).order_by('-date_pub')[:5]
        context['comment_form'] = self.comment_form
        return self.render_to_response(context)

    def post(self, request, ad_id, *args, **kwargs):
        self.object = self.get_object()
        form = self.comment_form(request.POST)
        if not request.user.is_authenticated:
            form.add_error(None, forms.ValidationError('Please log in to leave a comment'))
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.ad = self.object
            comment.save()

        context = self.get_context_data(object=self.object)
        context.update({
            'comments': Comment.objects.filter(ad__pk=ad_id).order_by('-date_pub')[:5],
            'comment_form': form,
        })
        return self.render_to_response(context)


class AdCreate(CreateView):
    form_class = AdCreateForm
    template_name = 'ads/ad_create.html'

    @login_required()
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
        author_rating, created = Rating.objects.get_or_create(user_who_rate=request.user, user_rated=ad.author)
        author_rating.rating_value = request.POST.get('selected_rating')
        author_rating.save()
    print(request)
    return redirect(request.META.get('HTTP_REFERER'), request)

