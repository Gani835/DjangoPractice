from django.urls import path
from .import views

urlpatterns = [
    path('',views.order),
    path('bill',views.bill),
]
