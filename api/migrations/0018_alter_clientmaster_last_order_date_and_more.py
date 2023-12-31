# Generated by Django 4.0.4 on 2023-06-29 04:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_transactions_txn_date_alter_voucher_last_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmaster',
            name='last_order_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='txn_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 4, 42, 50, 507008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='last_used',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 4, 42, 50, 507008, tzinfo=utc), null=True),
        ),
    ]
