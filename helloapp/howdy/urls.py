# howdy/urls.py
from django.conf.urls import url
from howdy import views
from django.urls import path
from . import contact


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^alive/$', views.AlivePageView.as_view()), # Add this /alive/ route
    path('contact/', contact.contact, name='contact'), # add contact form path
]
