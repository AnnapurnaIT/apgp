from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.


def homeView(request):

    return HttpResponse("hello world!")
@never_cache 
def AddPost(request):
    if request.method=='POST':
        Pform=forms.PostForm(request.POST)
        if Pform.is_valid():
            post=Pform.cleaned_data['post']
            models.Post.objects.create(name=post)

            return redirect('dcchome')
    else:
        Pform=forms.PostForm(request.POST)
    return render(request, 'dcc/allform.html',{'form':Pform})


@never_cache 
def AddEmployee(request):
    if request.method=='POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            
            models.Post.objects.create(**form.cleaned_data)

            return redirect('dcchome')
    else:
        Empform=forms.EmpForm(request.POST)
    return render(request, 'dcc/allform.html',{'form':Empform})

