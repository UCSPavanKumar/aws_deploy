# Generated by Django 4.0.4 on 2023-06-27 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_attendant_profile_alter_transactions_txn_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='txn_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 13, 50, 20, 573245, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='last_used',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 27, 13, 50, 20, 573245, tzinfo=utc), null=True),
        ),
    ]
