from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,QueryDict
def home(request):
    name=request.GET.get('name')
    message=request.GET.get('message')
    return render(request,'hellorekruto/home.html',{'name':name,'message':message})

