from django.urls import path
from.import views

urlpatterns = [
    path('',views.authenticating),
    path('signup',views.createuser),
    path('logout',views.userlogout),
    
]
