# Generated by Django 5.0.6 on 2024-06-17 10:22

import dcc.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcc', '0008_publicrep_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicrep',
            name='pubrep_weight',
            field=models.IntegerField(choices=dcc.models.Choices.IntegerChoices100, default=50),
        ),
    ]
