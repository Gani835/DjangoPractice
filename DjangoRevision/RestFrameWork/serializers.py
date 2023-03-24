from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeList
        fields='__all__'
        

        