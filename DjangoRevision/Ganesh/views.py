from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from.models import Employee
from .forms import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# To connect the database and fetching the data from database. . . .
def practice(request):
    context={}
    if request.method=='POST':
        cusid=request.POST['custid']
        cur=connection.cursor()
        cur.execute('select * from customers where customerid=%s',(cusid,))
        data=cur.fetchall()
        context['detailes']=data
        #print(data)
        return render(request,'customers.html',context)
    return render(request,'customers.html')

# O.R.M Technique(Without knowing of SQL queries we can create table in database)
# By using Python shell we can made CRUD operations. . . . .

# Creating a employee form by using HTML input tags. . . .
def insertemployee(request):
    if request.method=='POST':
        eid=request.POST['empid']
        ename=request.POST['empname']
        eage=request.POST['empage']
        esal=request.POST['empsal']
        edno=request.POST['empdeptno']
        edname=request.POST['empdeptname']
        detailes=Employee(EmployeeID=eid,EmployeeName=ename,EmployeeAge=eage,EmployeeSalary=esal,EmployeeDeptNo=edno,EmployeeDeptName=edname)
        detailes.save()
        return HttpResponse('Detailes saved successfully. . . . .')
    return render(request,'insertemployee.html')

def fetchemployee(request):
    context={}
    if request.method=='POST':
        eid=request.POST['empid']
        cur=connection.cursor()
        cur.execute('select * from ganesh_employee where EmployeeID=%s',(eid,))
        data=cur.fetchall()
        context['fetch']=data
        return render(request,'fetchemployee.html',context)
    return render(request,'fetchemployee.html')

# Creating Employee Form. .(Model converts into Form)

@login_required(login_url='loginpage')
def employeeform(request):
    context={}
    form=EmployeeForm()
    context['form']=form
    if request.method=='POST':
        data=EmployeeForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Form Created Successfully. . . .')
        else:
            form=EmployeeForm()
            context['empform']=form
    return render(request,'empform.html',context)
            
# Fetch the employee data simply. . . . 

def empfetch(request):
    context={}
    data=Employee.objects.all()
    context['details']=data
    return render(request,'fetchemp.html',context)

# Class Based Views. . . . 

class CreateStudent(CreateView):
    model=StudentDetailes
    fields='__all__'
    
class ListStudent(ListView):
    model=StudentDetailes
    fields='__all__'
    
class DetailStudent(DetailView):
    model=StudentDetailes
    fields='__all__'

class UpdateStudent(UpdateView):
    model=StudentDetailes
    fields='__all__'
    
class DeleteStudent(DeleteView):
    model=StudentDetailes
    fields='__all__'
    success_url='delete'
    
# Authentication. . . . 

def authentication(request):
    context={}
    empform=EmployeeForm()
    context['form']=empform
    if request.method=='POST':
        uname=request.POST['usname']
        pwd=request.POST['pswd']
        
        validuser=authenticate(username=uname,password=pwd)
        if validuser is not None:
            if request.user.is_authenticated:
                return render(request,'empform.html',context)
            else:
                login(request,validuser)
        else:
            return HttpResponse('Invalid User')
          
    return render(request,'loginpage.html')


def usersignup(request):
    context={}
    context['signupform']=UserCreationForm()
    if request.method=='POST':
        newuser=UserCreationForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return HttpResponse('Newuser created Successfully. . . .')
            return redirect('loginpage')
        
            #return HttpResponse('User created successfully. . . .')
        else:
            print(newuser.errors)
            return redirect('signup')
    return render(request,'usersignup.html',context)

def userlogout(request):
    logout(request)
    return render(request,'loginpage.html')