# Generated by Django 3.0.3 on 2020-03-24 21:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200324_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sticker_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.Sticker'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_on',
            field=models.DateField(default=datetime.datetime(2020, 3, 27, 23, 51, 25, 301219)),
        ),
        migrations.AlterField(
            model_name='sticker',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
