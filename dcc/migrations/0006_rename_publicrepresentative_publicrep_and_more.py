# Generated by Django 5.0.6 on 2024-06-17 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcc', '0005_alter_post_name_alter_publicrepresentativepost_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PublicRepresentative',
            new_name='PublicRep',
        ),
        migrations.RenameModel(
            old_name='PublicRepresentativePost',
            new_name='PublicRepPost',
        ),
    ]