from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,QueryDict
def hello(request):
    # request=request.GET(QueryDict('a=1&a=2&c=3'))
    # if request.method=='GET':
    #     return render('hellorekruto/hello.html')
    name = request.GET.get('name','rekruto')
    message = request.GET.get('message','hello')
    return render(request,'hellorekruto/hello.html',{'message':message,'name':name})
def home(request):
    return render(request,'hellorekruto/home.html')

# Create your views here.
