# Generated by Django 3.1.6 on 2021-07-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsourcecode',
            name='inputFile',
            field=models.CharField(max_length=500, null=True, verbose_name='inputFile'),
        ),
    ]
