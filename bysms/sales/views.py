from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def listorders(request):
    return HttpResponse("这是一个订单列表")
