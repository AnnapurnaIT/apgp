from django.db import models
from django.core.exceptions import ValidationError


#Choices Here
################################################


# global variables
ward=11
WardStrings=('१','२','३','४','५','६','७','८','९','१०','११')
class Choices:
    @classmethod
    def IntegerChoices100(cls):  #cls for class 
        return [(i, str(i)) for i in range(1,101)]
    
    @classmethod
    def StatusChoices(cls):
        return [(1,'वर्तमान'),(0,'पूर्व')]
    @classmethod
    def WardChoices(cls):
        return [(i,WardStrings[i-1]) for i in range(1,ward+1)]
    # @classmethod
    # def ServiceChoices(cls):
    #     return [
    #         (0,'नेपाल आर्थिक योजना तथा तथ्यांक सेवा'),
    #         (1,'नेपाल इन्जिनियरिङ सेवा'),
    #         (2, 'नेपाल कृषि सेवा'),    
    #             ]


################################################# 
class PublicRepPost(models.Model):
    name=models.CharField(max_length=100, verbose_name="जनप्रतिनिधि पद")
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200, verbose_name='कर्मचारि पद') 
    def __str__(self): 
        return self.name 

class Section(models.Model):
    sec_name = models.CharField(max_length=200, verbose_name='शाखा')
    sec_head = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True,
                                    blank=True, related_name='headed_section',
                                      verbose_name='शाखा प्रमुख')
    
    def __str__(self):
        return self.sec_name
    
    def clean(self):
        if self.sec_head and self.sec_head.section != self:
            raise ValidationError('शाखा प्रमुख सम्बन्धित शाखाको हुनुपर्दछ ।')

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
    

class PublicRep(models.Model):
    name=models.CharField(max_length=100,null=True)
    post=models.ForeignKey(PublicRepPost,
                           on_delete=models.SET_DEFAULT,default='',
                           related_name='PublicRepresentative')
    phone_number=models.PositiveBigIntegerField(unique=True,verbose_name='सम्पर्क नं')
    ward=models.PositiveIntegerField(choices=Choices.WardChoices,default=1)
    pubrep_weight=models.IntegerField(choices=Choices.IntegerChoices100,default=50)
    def __str__(self):
        return f"{self.name} {self.post}"

 