from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentDetailes
# Create your views here.

def first(request):
    return render(request,'index.html')