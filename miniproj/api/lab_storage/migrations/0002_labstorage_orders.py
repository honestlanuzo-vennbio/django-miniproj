# Generated by Django 3.2.5 on 2022-03-31 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('lab_storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labstorage',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
    ]
