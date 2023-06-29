# Generated by Django 4.0.4 on 2023-06-29 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_chat_created_at_alter_chat_chat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 10, 12, 22, 384499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='txn_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 10, 12, 22, 383499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='last_used',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 10, 12, 22, 383499, tzinfo=utc), null=True),
        ),
    ]
