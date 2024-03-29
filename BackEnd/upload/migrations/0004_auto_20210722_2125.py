# Generated by Django 3.2.5 on 2021-07-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20210716_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coderesult',
            name='bugs',
        ),
        migrations.RemoveField(
            model_name='coderesult',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='programresult',
            name='bugs',
        ),
        migrations.RemoveField(
            model_name='programresult',
            name='sample',
        ),
        migrations.AddField(
            model_name='coderesult',
            name='crashes',
            field=models.CharField(default='0', max_length=10, verbose_name='crashes'),
        ),
        migrations.AddField(
            model_name='coderesult',
            name='fuzzer',
            field=models.CharField(default='', max_length=20, verbose_name='fuzzer'),
        ),
        migrations.AddField(
            model_name='coderesult',
            name='programName',
            field=models.CharField(default='', max_length=100, verbose_name='programName'),
        ),
        migrations.AddField(
            model_name='coderesult',
            name='time',
            field=models.CharField(default='', max_length=12, verbose_name='time'),
        ),
        migrations.AddField(
            model_name='programresult',
            name='crashes',
            field=models.CharField(default='0', max_length=10, verbose_name='crashes'),
        ),
        migrations.AddField(
            model_name='programresult',
            name='fuzzer',
            field=models.CharField(default='', max_length=20, verbose_name='fuzzer'),
        ),
        migrations.AddField(
            model_name='programresult',
            name='time',
            field=models.CharField(default='', max_length=12, verbose_name='time'),
        ),
    ]
