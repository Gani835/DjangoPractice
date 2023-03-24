from django.urls import path
from .import views

urlpatterns=[
    path('',views.insprod),
    path('fetch',views.fetchprod),
    path('pform',views.prodform),
    path('pfetch',views.pfetch),
    
    path('fcreate',views.CreateFamily.as_view(),name='create'),
    path('flist',views.ListFamily.as_view()),
    path('fdetailes/<int:pk>',views.DetailFamily.as_view()),
    path('fupdate/<int:pk>',views.UpdateFamily.as_view()),
    path('fdelete/<int:pk>',views.DeleteFamily.as_view(),name='delete')
]