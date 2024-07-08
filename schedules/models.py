from django.db import models
from dcc.models import PublicRep

# Create your models here.

class PubRepSchedule(models.Model):
    PubRep=models.ForeignKey(PublicRep,on_delete=models.SET_DEFAULT, default='  ')
    
