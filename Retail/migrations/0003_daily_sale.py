# Generated by Django 3.2.4 on 2022-02-22 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0025_alter_complete_job_cost_com'),
        ('Retail', '0002_auto_20220222_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('d_sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Retail.customer_cart')),
                ('payment_reciept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Jobs.reciepts')),
                ('sale_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
