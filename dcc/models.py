from django.db import models
from django.core.exceptions import ValidationError


#Choices Here
################################################

class Choices:
    @classmethod
    def IntegerChoices100(cls):  #cls for class 
        return [(i, str(i)) for i in range(1,101)]
    
    @classmethod
    def StatusChoices(cls):
        return [(1,'वर्तमान'),(0,'पूर्व')]
    # @classmethod
    # def ServiceChoices(cls):
    #     return [
    #         (0,'नेपाल आर्थिक योजना तथा तथ्यांक सेवा'),
    #         (1,'नेपाल इन्जिनियरिङ सेवा'),
    #         (2, 'नेपाल कृषि सेवा'),    
    #             ]


################################################# 
class Post(models.Model):
    name = models.CharField(max_length=200) 
    def __str__(self): 
        return self.name

class Section(models.Model):
    sec_name = models.CharField(max_length=200)
    sec_head = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True,
                                    blank=True, related_name='headed_section')
    
    def __str__(self):
        return self.sec_name
    
    def clean(self):
        if self.sec_head and self.sec_head.section != self:
            raise ValidationError('The head must be an employee of the same section.')

class Employee(models.Model):
    
    # StatusChoices=[(1,'वर्तमान'),(0,'पूर्व')]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField(unique=True,blank=True, null=True)
    email = models.EmailField(default='hello@example.com')
    
    emp_post = models.ForeignKey(Post, on_delete=models.SET_DEFAULT,
                                    default=1, related_name='posts')
    
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,null=True, 
                                 default=1, related_name='employees')
    
    emp_weight = models.IntegerField(choices=Choices.IntegerChoices100, default=1)
    emp_status=models.IntegerField(choices=Choices.StatusChoices, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    serv_name = models.CharField(max_length=200)
    required_documents = models.TextField()
    serv_fee = models.PositiveIntegerField()
    serv_time = models.CharField(max_length=200)
    serv_section = models.ForeignKey(Section, on_delete=models.SET_DEFAULT,
                                      default=1, related_name='services')
    
