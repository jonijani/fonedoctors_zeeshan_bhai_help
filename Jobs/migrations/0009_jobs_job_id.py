# Generated by Django 3.2.4 on 2022-01-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0008_rename_acessories_jobs_accessories'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]