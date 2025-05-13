from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('campaigns/malware/', views.malware, name='malware'),
    path('campaigns/credential/', views.credential, name='credential'),
    path('campaigns/spear/', views.spear, name='spear'),
    path('campaigns/fakelogin/', views.fakelogin, name='fakelogin'),
]
