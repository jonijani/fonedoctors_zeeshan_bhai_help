# Generated by Django 3.2.4 on 2022-01-20 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_customer_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_time',
            new_name='created_date',
        ),
    ]
