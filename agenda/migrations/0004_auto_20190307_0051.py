# Generated by Django 2.1.5 on 2019-03-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20190305_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('D', 'Dinheiro'), ('CD', 'Cartão Debito'), ('CC', 'Cartão Credito')], max_length=2, null=True, verbose_name='Pagamento'),
        ),
    ]
