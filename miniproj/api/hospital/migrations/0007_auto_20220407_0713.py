# Generated by Django 3.2.5 on 2022-04-07 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20220401_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Please use letters only.')]),
        ),
    ]
