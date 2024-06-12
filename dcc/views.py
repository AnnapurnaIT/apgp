from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from . import form
from . import models

# Create your views here.


def homeView(request):

    return HttpResponse("hello world!")
@never_cache 
def AddPost(request):
    if request.method=='POST':
        Pform=form.PostForm(request.POST)
        if Pform.is_valid():
            post=Pform.cleaned_data['post']
            models.Post.objects.create(name=post)

            return redirect('dcchome')
    else:
        Pform=form.PostForm(request.POST)
    return render(request, 'dcc/allform.html',{'form':Pform})


