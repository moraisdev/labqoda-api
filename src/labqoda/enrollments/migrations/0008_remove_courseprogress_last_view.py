# Generated by Django 3.0.9 on 2020-08-27 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0007_courseprogress_last_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseprogress',
            name='last_view',
        ),
    ]
