# Generated by Django 3.2.5 on 2022-04-07 07:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20220407_0713'),
        ('lab_storage', '0004_labstorage_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labstorage',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\.\\-\\, ]*$', 'Only letters, numbers, periods, hyphens and commas are allowed.')]),
        ),
        migrations.AlterField(
            model_name='labstorage',
            name='orders',
            field=models.ManyToManyField(limit_choices_to={'is_deleted': False}, to='order.Order'),
        ),
    ]
