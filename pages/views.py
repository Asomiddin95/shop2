from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from pages.forms import ContactModelForm
from posts.views import PostModel
from product.views import ProductModel
from django.urls import reverse


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        context['products'] = ProductModel.objects.order_by('-pk')[:4]
        return context


class ContactCreatView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
