# Generated by Django 3.0.7 on 2020-06-14 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200614_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='_content',
            new_name='content',
        ),
    ]
