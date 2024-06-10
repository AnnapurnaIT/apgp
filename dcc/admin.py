from django.contrib import admin
from django.db.models import Model
from . import models

app_models = models.__dict__

for model_name in app_models:
    model = app_models[model_name] 
    if isinstance(model, type) and issubclass(model, Model):
        admin.site.register(model)