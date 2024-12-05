
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('About us',views.Aboutus,name='About us'),
    path('Noh',views.Noh,name='Noh'),
    path('fof',views.fof,name='fof'),
    path('PB',views.PB,name='PB'),
    path('AN',views.AN,name='AN'),
    path('contact',views.contact,name='contact'),
    path('products',views.products,name='products'),
    path('milk',views.milk,name='milk'),
    path('malai dahi',views.mdahi,name='malai dahi')





]



