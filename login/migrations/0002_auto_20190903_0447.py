# Generated by Django 2.2.5 on 2019-09-03 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='person',
            name='modification_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='modification_time',
        ),
        migrations.AddField(
            model_name='person',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AddField(
            model_name='person',
            name='modification_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modification Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='modification_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modification Date'),
        ),
    ]
