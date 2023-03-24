from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    s="<h1>This is first resp</h1>"
    return HttpResponse(s)

def view2(request):
    n1=int(input('Enter a number'))
    n2=int(input('Enter a number'))
    n3=n1+n2
    return HttpResponse(str(n3))
