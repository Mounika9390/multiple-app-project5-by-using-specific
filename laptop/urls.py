from laptop.views import *
from django.urls import path
app_name='Electonic Gadget2'
urlpatterns=[
    path('lenovo/',lenovo,name='lenovo'),
    path('dell/',dell,name='dell'),
]