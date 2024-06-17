from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from . import forms
from . import models


#defining some reusable variables
form_classes={
    
    'post':(forms.PostForm, models.Post),
    'emp':(forms.EmpForm,models.Employee),
    # 'serv':(forms.ServiceForm,models.Service),
    'sec': (forms.SectionForm,models.Section),
    'pubRep':(forms.PublicRepForm,models.PublicRep),
    'pubRepPost':(forms.PublicRepPostForm,models.PublicRepPost), 
}
# object_classes={
#     'post':models.Post,
#     'pPost':models.PublicRepresentativePost,
#     'emp': models.Employee,
#     'sec': models.Section,
#     'serv':models.Service,
#     'pubrep':models.PublicRepresentative
# }


# Create your views here.
def AddNew(request, form_type):

    if form_type not in form_classes:
        return redirect('dcchome')
    form_class, model_class=form_classes[form_type]
    # return HttpResponse(form_classes[form_type])

    if request.method == 'POST':
        form=form_class(request.POST)
        if form.is_valid():
            model_class.objects.create(**form.cleaned_data)
            return redirect ('dcchome')
    else:
        form=form_class(request.POST)
    return render(request,'dcc/allform.html',{'form':form})


def homeView(request):
    return render(request,'dcc/home.html')

    
def EmpListView(request):
    emps=models.Employee.objects.all()
    return render(request,'dcc/emplist.html', {'emps': emps})

    
  


# @never_cache 
# def AddPost(request):
#     if request.method=='POST':
#         Pform=forms.PostForm(request.POST)
#         if Pform.is_valid():
#             post=Pform.cleaned_data['post']
#             models.Post.objects.create(name=post)

#             return redirect('dcchome')
#     else:
#         Pform=forms.PostForm(request.POST)
#     return render(request, 'dcc/allform.html',{'form':Pform})


# @never_cache 
# def AddEmployee(request):
#     if request.method=='POST':
#         form=forms.EmpForm(request.POST)
#         if form.is_valid():
            
#             models.Employee.objects.create(**form.cleaned_data)

#             return redirect('dcchome')
#     else:
#         form=forms.EmpForm(request.POST)
#     return render(request, 'dcc/allform.html',{'form':form})

# @never_cache 
# def AddSection(request, form_type):
    
    
#     if request.method=='POST':
#         form=forms.SectionForm(request.POST)
#         if form.is_valid():
            
#             models.Section.objects.create(**form.cleaned_data)

#             return redirect('dcchome')
#     else:
#         form=forms.SectionForm(request.POST)
#     return render(request, 'dcc/allform.html',{'form':form})