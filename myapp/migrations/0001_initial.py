# Generated by Django 3.0.3 on 2020-02-13 23:30

import datetime
from django.db import migrations, models
import django.utils.timezone
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=10, null=True)),
                ('building_number', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('delivery_on', models.DateField(default=datetime.datetime(2020, 2, 17, 1, 30, 28, 41547))),
                ('delivery_status', models.BooleanField(choices=[(True, 'complete'), (False, 'incomplete')], default=False)),
                ('sticker_id', models.IntegerField(blank=True)),
                ('name_field', models.CharField(max_length=40)),
                ('class_field', models.CharField(blank=True, max_length=40, null=True)),
                ('school_field', models.CharField(blank=True, max_length=40, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('stickerImage', models.ImageField(blank=True, null=True, upload_to=myapp.models.imagePath)),
                ('added_notes', models.TextField(blank=True, max_length=100, null=True)),
                ('order_status', models.BooleanField(choices=[(True, 'complete'), (False, 'incomplete')], default=False)),
                ('ordered_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_fees', models.PositiveIntegerField()),
                ('delivery_fees', models.PositiveIntegerField()),
                ('total_fees', models.PositiveIntegerField()),
            ],
        ),
    ]