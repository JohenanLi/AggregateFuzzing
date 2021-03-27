# Generated by Django 3.1.6 on 2021-03-15 11:54

from django.db import migrations, models
import django.db.models.deletion
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsourcecode',
            name='filePath',
            field=models.FileField(upload_to=upload.models.upload_to, verbose_name='filePath'),
        ),
        migrations.AlterField(
            model_name='uploadsourcecode',
            name='inputFile',
            field=models.FileField(upload_to=upload.models.uploadInput, verbose_name='inputFile'),
        ),
        migrations.AlterField(
            model_name='uploadsourcecode',
            name='ins',
            field=models.TextField(max_length=500, verbose_name='seeddir'),
        ),
        migrations.AlterField(
            model_name='uploadsourceprogram',
            name='filePath',
            field=models.FileField(upload_to=upload.models.upload_to, verbose_name='filePath'),
        ),
        migrations.AlterField(
            model_name='uploadsourceprogram',
            name='inputFile',
            field=models.FileField(upload_to=upload.models.uploadInput, verbose_name='inputFile'),
        ),
        migrations.AlterField(
            model_name='uploadsourceprogram',
            name='ins',
            field=models.TextField(max_length=1000, verbose_name='seeddir'),
        ),
        migrations.CreateModel(
            name='programResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('codeCoverage', models.CharField(max_length=10, verbose_name='codeCoverage')),
                ('bugs', models.TextField(max_length=1000, verbose_name='bugs')),
                ('sample', models.CharField(max_length=100, verbose_name='sample')),
                ('program', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='upload.uploadsourceprogram')),
            ],
        ),
        migrations.CreateModel(
            name='codeResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('codeCoverage', models.CharField(max_length=10, verbose_name='codeCoverage')),
                ('bugs', models.TextField(max_length=1000, verbose_name='bugs')),
                ('sample', models.CharField(max_length=100, verbose_name='sample')),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='upload.uploadsourcecode')),
            ],
        ),
    ]