from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('malware', views.malware, name='malware'),
    path('credential', views.credential, name='credential'),
    path('spear', views.spear, name='spear'),
    path('fakelogin', views.fakelogin, name='fakelogin'),
]