from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def apple(request):
    return HttpResponse('this is the best tab')