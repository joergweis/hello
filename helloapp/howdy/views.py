 # howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add About view
class AboutPageView(TemplateView):
    template_name = "about.html"

# Add Alive view
class AlivePageView(TemplateView):
    template_name = "alive.html"
