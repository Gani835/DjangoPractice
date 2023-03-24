from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

                # # # MIXINS # # #
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

                # # # Concrete Generic View Class # # #
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

@api_view(['GET'])
def first(request):
    return Response({'status':200,'message':'This is the rest framework api. . . .'})

# Serializer:- Serializer works very similar to Django forms and ModelForm classes.
# Serializers converts objects into datatypes understandable by JS and Front-end frameworks.
# Serializers are of Two types 1) Model Serializer  2) Hyperlinked Model Serializer

# 1) Create an API:-

@api_view(['POST'])
def poststudent(request):
    obj=Student.objects.all()
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# 2) Read an API:-

@api_view(['GET'])
def getstudent(request):
    obj=Student.objects.all()
    serializer=StudentSerializer(obj,many=True)
    return Response(serializer.data)

# 3) Update an API:-

@api_view(['POST'])
def updatestudent(request,id):
    obj=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# 4) Delete an API:-

@api_view(['DELETE'])
def deletestudent(request,id):
    obj=Student.objects.get(id=id)
    obj.delete()
    return Response('One Student API was Deleted Successfully. . . . .')

                # # # Generic API View MIXINS Concept # # # 

# 1) CreateModelMixin:- (post method)

class EmployeeCreate(GenericAPIView,CreateModelMixin):
    queryset=EmployeeList.objects.all()
    serializer_class=EmployeeListSerializer
    
    def post(self,request):
        return self.create(request)
        
# 2) ListModelMixin:- (get method)

class EmployeeList(GenericAPIView,ListModelMixin):
    queryset=EmployeeList.objects.all()
    serializer_class=EmployeeListSerializer
    
    def get(self,request):
        return self.list(request)
    
# 3) RetrieveModelMixin:- (get method)

'''class EmployeeRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=EmployeeList.objects.all()
    serializer_class=EmployeeListSerializer
    
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    
# 4) UpdateModelMixin:- (put method)

class EmployeeUpdate(GenericAPIView,UpdateModelMixin):
    queryset=EmployeeList.objects.all()
    serializer_class=EmployeeListSerializer
    
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
#5) DestoyModelMixin:- (delete method)

class EmployeeDelete(GenericAPIView,DestroyModelMixin):
    queryset=EmployeeList.objects.all()
    serializer_class=EmployeeListSerializer
    
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    
# Concrete Generic view class. . . . . 

# 1) CreateAPIView:-

class EmployeeCrateAPIView(CreateAPIView):
    queryset=EmployeeList.objects.all()
    serializer_class=EmployeeListSerializer'''
    
    
