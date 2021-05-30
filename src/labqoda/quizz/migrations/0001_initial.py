# Generated by Django 3.0.1 on 2020-04-27 20:36

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('single_choices', 'Single Choice'), ('multi_choices', 'Multiple Choices')], default='single_choices', max_length=20)),
                ('justification', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=1)),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Content')),
                ('questions', models.ManyToManyField(to='quizz.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]