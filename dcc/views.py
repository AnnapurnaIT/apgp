from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
# Create your views here.


def homeView(request):

    return HttpResponse("hello world!")