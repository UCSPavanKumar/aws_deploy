# Generated by Django 4.0.4 on 2023-06-19 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_clientmaster_last_order_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='agent_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='balance',
            new_name='left_balance',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='txn_amount',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='voucher_id',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='txn_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
