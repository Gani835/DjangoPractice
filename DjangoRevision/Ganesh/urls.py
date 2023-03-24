from django.urls import path
from.import views

urlpatterns = [
    path('',views.practice),
    path('insert',views.insertemployee),
    path('fetch',views.fetchemployee),
    path('create',views.employeeform),
    path('empfetch',views.empfetch),
    
    path('createstudent',views.CreateStudent.as_view()),
    path('liststudent',views.ListStudent.as_view()),
    path('detailstudent/<pk>',views.DetailStudent.as_view()),
    path('updatestudent/<pk>',views.UpdateStudent.as_view()),
    path('deletestudent/<pk>',views.DeleteStudent.as_view(),name='delete'),
    
    path('auth',views.authentication,name='loginpage'),
    path('logout',views.userlogout),
    path('signup',views.usersignup,name='signup'),
]
