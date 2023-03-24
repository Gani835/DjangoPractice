from django.urls import path
from.import views

urlpatterns = [
    path('',views.first),
    path('post',views.poststudent),
    path('get',views.getstudent),
    path('update/<int:id>/',views.updatestudent),
    path('delete/<int:id>/',views.deletestudent),
    
    path('create',views.EmployeeCreate.as_view()),
    path('list',views.EmployeeList.as_view()),
    #path('retrieve/<int:pk>/',views.EmployeeRetrieve.as_view()),
    #path('update/<int:pk>/',views.EmployeeUpdate.as_view()),
    #path('delete/<int:pk>/',views.EmployeeDelete.as_view()),
    
    # Class Based API Views. . . . 
    #path('createAPI',views.EmployeeCrateAPIView.as_view()),
    
    
]
