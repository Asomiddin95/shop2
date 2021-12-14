from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from pages.forms import ContactModelForm
from django.urls import reverse


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class ContactCreatView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
