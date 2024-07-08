

from django.urls import path
from . import views

# urls here
urlpatterns = [
    path('add/<str:form_type>/', views.AddNew, name='addnew'),
    path('',views.homeView, name='dcchome'),
    path('employees',views.EmpListView, name='employee_list'),
    path('pubreps', views.PubRepView, name='pubrep_list'),
    path('posts/<str:post_type>/', views.PostView, name='postlist')
    # path('add',views.AddPost, name='addPost'),
    # path('add',views.AddEmployee, name='addEmployee'),
]




