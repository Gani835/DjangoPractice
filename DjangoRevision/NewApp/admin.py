from django.contrib import admin
from .models import StudentDetailes
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    l=['number','name','marks']
    
admin.site.register(StudentDetailes,StudentAdmin)