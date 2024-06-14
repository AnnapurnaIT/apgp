

from django.urls import path
from . import views

# urls here
urlpatterns = [
    path('add/<str:form_type>/', views.AddNew, name='addnew'),
    path('',views.homeView, name='dcchome'),
    # path('add',views.AddPost, name='addPost'),
    # path('add',views.AddEmployee, name='addEmployee'),
    

]




