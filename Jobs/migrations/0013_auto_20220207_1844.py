# Generated by Django 3.2.4 on 2022-02-07 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_created_by'),
        ('Jobs', '0012_job_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_update',
            name='job',
        ),
        migrations.AddField(
            model_name='job_update',
            name='accessories_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories_update', to='Jobs.accessories'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='collection_time_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job_update',
            name='cost_update',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job_update',
            name='customer_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_update', to='customer.customer'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='device_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_update', to='Jobs.devices'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='fault_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fault_update', to='Jobs.fault'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='imei_update',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='job_update',
            name='job_status_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_status_update', to='Jobs.job_status'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='job_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_update', to='Jobs.jobs'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='make_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='make_update', to='Jobs.make'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='model_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_update', to='Jobs.model'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='network_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='network_update', to='Jobs.network'),
        ),
        migrations.AddField(
            model_name='job_update',
            name='passcode_update',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='job_update',
            name='payment_status_update',
            field=models.CharField(blank=True, choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID'), ('CREDIT NOTE', 'CREDIT NOTE'), ('REFUND', 'REFUND')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='job_update',
            name='sale_item_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_sale_item', to='Jobs.sale_item'),
        ),
        migrations.AlterField(
            model_name='job_update',
            name='description_update',
            field=models.TextField(blank=True, null=True),
        ),
    ]
