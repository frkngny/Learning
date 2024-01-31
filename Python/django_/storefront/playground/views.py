from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    # you can do anything here .gh
    return HttpResponse("Hello World")

def say_hi(request):
    return render(request, 'hello.html', {'name': 'Furkan', 'srn': 'Güney'})