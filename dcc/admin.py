from django.contrib import admin
from . import models
# Register your models here.

app_models = models.__dict__

# admin.site.register(Employee)
# admin.site.register(Section)

for model_name in app_models:
    model = app_models[model_name] 
    if isinstance(models, type) and issubclass(models, models.Model):
        admin.site.register(model)

