from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contacto/', views.contact, name='contact'),
    path('hacemos/', views.hacemos, name='hacemos'),
    path('testing/', views.testing, name='testing'),
]
