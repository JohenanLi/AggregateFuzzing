# Generated by Django 3.1.6 on 2021-03-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20210324_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsourcecode',
            name='ins',
            field=models.TextField(default='', max_length=500, verbose_name='seeddir'),
        ),
        migrations.AlterField(
            model_name='uploadsourceprogram',
            name='ins',
            field=models.TextField(default='', max_length=1000, verbose_name='seeddir'),
        ),
    ]
