# Generated by Django 3.2.4 on 2022-03-01 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0033_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivered',
            name='customer_deliver',
        ),
    ]
