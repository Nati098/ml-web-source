# Generated by Django 3.0.7 on 2020-06-13 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200613_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='webdemo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='public_date'),
            preserve_default=False,
        ),
    ]
