# Generated by Django 3.0.3 on 2020-03-24 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200221_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Basic', 'Basic'), ('Boy', 'Boys'), ('Girl', 'Girls'), ('Youth', 'Youth')], max_length=30)),
                ('sticker_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_on',
            field=models.DateField(default=datetime.datetime(2020, 3, 27, 23, 19, 16, 360856)),
        ),
    ]
