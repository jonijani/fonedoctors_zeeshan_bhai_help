# Generated by Django 3.2.4 on 2022-01-26 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0003_auto_20220126_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_device', to='Jobs.devices'),
        ),
    ]
