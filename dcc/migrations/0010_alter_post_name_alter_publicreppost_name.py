# Generated by Django 5.0.6 on 2024-06-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcc', '0009_publicrep_pubrep_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200, verbose_name='कर्मचारि पद'),
        ),
        migrations.AlterField(
            model_name='publicreppost',
            name='name',
            field=models.CharField(max_length=100, verbose_name='जनप्रतिनिधि पद'),
        ),
    ]
