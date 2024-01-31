from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sumi(request):
    return HttpResponse ('<h>i am good girl<h\>')