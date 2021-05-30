# Generated by Django 3.0.6 on 2020-05-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Pagina de Contato', 'verbose_name_plural': 'Pagina de Contatos'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=120, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='mensagem'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=120, verbose_name='nome'),
        ),
    ]