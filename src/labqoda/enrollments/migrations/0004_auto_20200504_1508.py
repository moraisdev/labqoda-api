# Generated by Django 3.0.5 on 2020-05-04 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200429_1021'),
        ('enrollments', '0003_auto_20200429_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathenrollment',
            name='enrollment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollments.Enrollment'),
        ),
        migrations.AlterField(
            model_name='pathenrollment',
            name='path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Path', verbose_name='Path'),
        ),
        migrations.AlterUniqueTogether(
            name='pathenrollment',
            unique_together=set(),
        ),
    ]
