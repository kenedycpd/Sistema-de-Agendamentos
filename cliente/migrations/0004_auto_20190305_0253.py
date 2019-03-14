# Generated by Django 2.1.5 on 2019-03-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_person_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nome',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='telefone',
            field=models.CharField(blank=True, max_length=9, verbose_name='Telefone'),
        ),
    ]
