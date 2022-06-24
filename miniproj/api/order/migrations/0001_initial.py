# Generated by Django 3.2.5 on 2022-03-31 06:52

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import miniproj.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sample', '0001_initial'),
        ('physician', '0001_initial'),
        ('hospital', '0005_alter_hospital_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('internal_id', models.CharField(max_length=255)),
                ('date_sample_taken', models.DateTimeField(auto_now_add=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('status', enumfields.fields.EnumField(default='Received', enum=miniproj.constants.OrderStatus, max_length=30, null=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hospital')),
                ('physician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='physician.physician')),
                ('sample', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.sample')),
            ],
            options={
                'verbose_name': 'Order List',
                'ordering': ['internal_id'],
            },
        ),
    ]
