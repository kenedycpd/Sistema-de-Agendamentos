# Generated by Django 2.1.5 on 2019-03-05 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20190227_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='genero',
        ),
    ]