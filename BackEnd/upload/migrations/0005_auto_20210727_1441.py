# Generated by Django 3.2.5 on 2021-07-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20210722_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadsourcecode',
            name='hour',
            field=models.CharField(blank=True, default='', max_length=3, verbose_name='hour'),
        ),
        migrations.AddField(
            model_name='uploadsourcecode',
            name='minute',
            field=models.CharField(blank=True, default='', max_length=4, verbose_name='minute'),
        ),
    ]
