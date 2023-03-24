from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def order(request):
    context={}
    context['orderform']=OrderForm()
    if request.method=='POST':
        data=OrderForm(request.POST)
        if data.is_valid():
            data.save()
            return render(request,'bill.html')
            #return HttpResponse('Your Order Created Successfully. . . .')
        else:
            context={}
            context['orderform']=OrderForm()
    return render(request,'orderform.html',context)


def bill(x):
    price=("select Quantity from gani835.bill_order where id=1;")*x
    return price
res=bill(20)
print(res)