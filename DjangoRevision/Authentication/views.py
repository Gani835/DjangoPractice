from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from Ganesh.models import *
from Ganesh.forms import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def authenticating(request):
    context={}
    context['form']=EmployeeForm()
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
            return HttpResponse('Invaliduser')
    return render(request,'login.html')

def createuser(request):
    context={}
    form=SignupForm()
    context['signupform']=form
    if request.method=='POST':
        newuser=SignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return HttpResponse('New User Created Successfully. . . .')
        else:
            return redirect('signup')
    return render(request,'signupform.html',context)

def userlogout(request):
    logout(request)
    return render(request,'login.html')

