from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView,RedirectView

class childRedict(RedirectView):
    url = 'https://www.facebook.com'