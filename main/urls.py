from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', home, name='home'),
  path('about/', about, name='about'),
  path('service/', service, name='service'),
  path('price/', price, name='price'),
  path('team/', team, name='team'),
  path('contact/', contact, name='contact'),
  path('sendmail/', sendmail, name='sendmail'),
  
  ]