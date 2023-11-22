from mobile.views import *
from django.urls import path
app_name='Electonic Gadget1'
urlpatterns=[
    path('vivo/',vivo,name='vivo'),
    path('iphone/',iphone,name='iphone'),

]