# Generated by Django 3.2.4 on 2022-03-02 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0038_auto_20220301_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='delivery_comments',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
