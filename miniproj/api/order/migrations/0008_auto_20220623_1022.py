# Generated by Django 3.2.5 on 2022-06-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_date_sample_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
