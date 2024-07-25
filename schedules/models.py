from django.db import models
from dcc.models import PublicRep
from nepali_datetime_field.models import NepaliDateField


# Create your models here.

class PubRepSchedule(models.Model):
    PubRep=models.ForeignKey(PublicRep,on_delete=models.SET_DEFAULT, default='  ')
    location=models.CharField(max_length=300)
    program_name=models.CharField(max_length=300)
    date=NepaliDateField()
    

    
