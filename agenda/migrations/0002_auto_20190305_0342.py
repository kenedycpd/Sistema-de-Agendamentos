# Generated by Django 2.1.5 on 2019-03-05 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('AD', 'Avista Dinheiro'), ('CD', 'Cartão de Debito'), ('CC', 'Cartão de Credito')], max_length=2, null=True, verbose_name='Pagamento'),
        ),
    ]