from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView

# Create your views here.


class EmployeeList(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    filterset_fields=['Location']