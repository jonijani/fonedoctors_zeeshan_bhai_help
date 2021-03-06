# Generated by Django 3.2.4 on 2022-03-07 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0040_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pictures',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
