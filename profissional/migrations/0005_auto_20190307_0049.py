# Generated by Django 2.1.5 on 2019-03-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0004_auto_20190307_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('D', 'Dinheiro'), ('CD', 'Cartão Debito'), ('CC', 'Cartão Credito')], max_length=2, verbose_name='Pagamento'),
        ),
    ]