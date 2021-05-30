# Generated by Django 3.0.6 on 2020-05-28 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0006_courseprogress_date_of_issue'),
        ('certificates', '0003_auto_20200511_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollments.CourseProgress')),
            ],
        ),
    ]
