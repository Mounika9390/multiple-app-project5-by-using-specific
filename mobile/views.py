from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vivo(request):
    return render(request,'vivo.html')
def iphone(request):
    return HttpResponse('Trending phone')