from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def test(request):
    return render(request, "test.html")

def add_numbers(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        result = num1 + num2
        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'add.html')

class testview(viewsets.ModelViewSet):
    serializer_class = testserials
    queryset  =  testmodel.objects.all()
