from django.urls import path
from.import views

urlpatterns = [
    path('',views.sentemail,name='email')
]
