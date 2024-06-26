# Generated by Django 5.0.6 on 2024-06-16 23:50

import dcc.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcc', '0003_alter_employee_phone_number_alter_employee_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicRepresentativePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PublicRepresentative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.PositiveIntegerField(choices=dcc.models.Choices.WardChoices, default=1)),
                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='PublicRepresentative', to='dcc.publicrepresentativepost')),
            ],
        ),
    ]
