from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db import connection
from .forms import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

# 1st Method:-

def insprod(request):
    if request.method=='POST':
        pid=request.POST['id']
        pcat=request.POST['cat']
        pname=request.POST['name']
        pprice=request.POST['price']
        
        detailes=ProductsDetailes(Product_ID=pid,Product_Category=pcat,Product_Name=pname,Product_Price=pprice)
        detailes.save()
        return HttpResponse('Product detailes added. . . .')
    return render(request,'insprod.html')

def fetchprod(request):
    context={}
    if request.method=='POST':
        prodid=request.POST['pid']
        cur=connection.cursor()
        cur.execute('select * from djangopractice_productsdetailes where product_id=%s',(prodid,))
        data=cur.fetchall()
        context['proddetailes']=data
        return render(request,'fetchprod.html',context)
    return render(request,'fetchprod.html')

# 2nd Method:-

def prodform(request):
    context={}
    form=ProductForm()
    context['prodform']=form
    if request.method=='POST':
        data=ProductForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Product form created successfully. . .')
        else:
            form=ProductForm()
            context['prodform']=form
    return render(request,'prodform.html',context)

def pfetch(request):
    context={}
    data=ProductsDetailes.objects.all()
    context['fetch']=data
    return render(request,'pfetch.html',context)

# Class Based Views. . . . 

class CreateFamily(CreateView):
    model=FamilyDetailes
    fields='__all__'
    success_url='create'
    
class ListFamily(ListView):
    model=FamilyDetailes
    fields='__all__'
    
class DetailFamily(DetailView):
    model=FamilyDetailes
    fields='__all__'

class UpdateFamily(UpdateView):
    model=FamilyDetailes
    fields='__all__'
    
class DeleteFamily(DeleteView):
    model=FamilyDetailes
    success_url='delete'
    
    def __str__(self):
        return self.Father_Name