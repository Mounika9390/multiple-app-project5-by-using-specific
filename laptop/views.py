from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lenovo(request):
    return HttpResponse('Best Laptop')
def dell(request):
    return HttpResponse('so many colleges using dell laptop for lab purpose and goverent exams')