# Generated by Django 3.0.6 on 2020-05-06 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20200429_1021'),
        ('enrollments', '0004_auto_20200504_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseenrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Course', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='courseprogress',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='courseprogress',
            name='course_enrollment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enrollments.CourseEnrollment'),
        ),
        migrations.AlterField(
            model_name='courseprogress',
            name='path_enrollment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enrollments.PathEnrollment'),
        ),
        migrations.AlterField(
            model_name='courseprogress',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
    ]
