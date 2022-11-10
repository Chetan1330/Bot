from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charge', views.payment, name="charge"),
    path('paypal', views.paypal, name="paypal"),
    path('upload', views.upload, name="upload"),
    path('stripe', views.htmlstripe, name="stripe"),
    path('withdraw', views.withdraw, name="withdraw"),
    path('paypalsucess', views.paypalsucess, name="paypalsucess"),
    path('success/<str:args>', views.sucess, name="success"),



    re_path(r'^.*\.*', views.pages, name='pages'),
    

]
