# Generated by Django 3.2.4 on 2022-03-01 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0032_jobs_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_deliver', models.TextField(blank=True, null=True)),
                ('imei_deliver', models.CharField(blank=True, max_length=250, null=True)),
                ('passcode_deliver', models.CharField(blank=True, max_length=250, null=True)),
                ('cost_deliver', models.IntegerField(blank=True, null=True)),
                ('collection_time_deliver', models.DateTimeField(blank=True, null=True)),
                ('payment_status_deliver', models.CharField(blank=True, choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID'), ('CREDIT NOTE', 'CREDIT NOTE'), ('REFUND', 'REFUND')], max_length=250, null=True)),
                ('delivered_on', models.DateTimeField(blank=True, null=True)),
                ('accessories_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories_deliver', to='Jobs.accessories')),
                ('customer_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_deliver', to='customer.customer')),
                ('delivered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('device_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_deliver', to='Jobs.devices')),
                ('fault_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fault_deliver', to='Jobs.fault')),
                ('job_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_deliver', to='Jobs.jobs')),
                ('job_status_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_status_deliver', to='Jobs.job_status')),
                ('make_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='make_deliver', to='Jobs.make')),
                ('model_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_deliver', to='Jobs.model')),
                ('network_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='network_deliver', to='Jobs.network')),
                ('sale_item_deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_item_deliver', to='Jobs.sale_item')),
            ],
        ),
    ]
