from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse('<h1> i love u amma</h1>')

def second(request):
    return HttpResponse('<h1><i>my brother is my best friend</i></h1>')

