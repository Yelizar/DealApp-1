# Generated by Django 3.0.3 on 2020-02-18 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='subject',
        ),
    ]
