from django.shortcuts import render
from.models import *
from .serializers import *

from rest_framework.generics import ListAPIView
# Create your views here.

# Pagination concept in REST API:-

class PeopleList(ListAPIView):
    queryset=People.objects.all()
    serializer_class=PeopleSerializer
    
    def get_queryset(self):
        user=self.request.user
        return People.objects.filter(passby=user)