# Generated by Django 5.1.5 on 2025-01-18 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='datatime_post',
            new_name='datatime_send',
        ),
    ]
