from django.db import models
from django.core.exceptions import ValidationError
import re
 
# Create your models here.
class post(models.Model):
    name=models.CharField(max_length=200)


class Section(models.Model):
    sec_name=models.CharField(max_length=200)
    sec_head=models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='headed_section'
                                   )
    def __str__(self):
        return self.sec_name
    def clean(self):
        if self.sec_head and self.sec_head.section !=self:
            raise ValidationError('the head must be an employee of the same section. ')

class Employee(models.Model):
    VALUE_CHOICES = [(i, str(i)) for i in range(1, 100)]
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.PositiveBigIntegerField(blank=True, null=True)
    email=models.EmailField(default='hello')
    emp_post=models.OneToOneField(post,on_delete=models.SET_DEFAULT,
                                   default='Admin',related_name='posts'
                                   )
    section=models.ForeignKey(Section, on_delete=models.SET_DEFAULT, 
                              default='Admin',related_name='employees')
    emp_weigth=models.IntegerField(choices=VALUE_CHOICES, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Service(models.Model):
    serv_name=models.CharField(max_length=200)
    required_documents=models.TextField()
    serv_fee=models.PositiveIntegerField()
    serv_time=models.CharField(max_length=200)
    serv_section=models.ForeignKey(Section,on_delete=models.SET_DEFAULT,
                                   default="Admin", related_name='services'
                                   )
    
