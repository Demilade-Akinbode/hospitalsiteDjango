from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hpms-home'),
    path('about/', views.about, name='hpms-about'),
    path('contact/', views.contact, name='hpms-contact'),
    path('services/', views.services, name='hpms-services'),
    path('appointment/', views.appointment, name='hpms-appointment'),
]