# Generated by Django 3.2.4 on 2022-01-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0006_rename_acessories_accessories_accessories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='payment_status',
            field=models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID'), ('CREDIT NOTE', 'CREDIT NOTE'), ('REFUND', 'REFUND')], max_length=250),
        ),
    ]
