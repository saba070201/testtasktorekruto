from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,QueryDict
def hello(request):
    name = request.GET.get('name','rekruto')
    message = request.GET.get('message','hello')
    return render(request,'hellorekruto/hello.html',{'message':message,'name':name})
def home(request):
    return render(request,'hellorekruto/home.html')

