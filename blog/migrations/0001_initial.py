# Generated by Django 4.2.1 on 2023-06-03 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('image', models.ImageField(upload_to='blog/images')),
                ('url', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]
