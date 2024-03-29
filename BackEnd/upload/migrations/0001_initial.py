# Generated by Django 3.1.6 on 2021-04-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploadSourceCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('filePath', models.TextField(max_length=500, verbose_name='filePath')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('ins', models.TextField(default='', max_length=500, null=True, verbose_name='seeddir')),
                ('inputFile', models.CharField(max_length=500, verbose_name='inputFile')),
                ('compileCommand', models.CharField(default='', max_length=100, verbose_name='compileCommand')),
                ('parameter', models.CharField(blank=True, default='', max_length=100, verbose_name='parameter')),
                ('inputCommand', models.TextField(blank=True, default='', max_length=500, verbose_name='inputCommand')),
            ],
        ),
        migrations.CreateModel(
            name='uploadSourceProgram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('filePath', models.CharField(max_length=50, verbose_name='filePath')),
                ('name', models.CharField(default='', max_length=100, verbose_name='name')),
                ('parameter', models.CharField(blank=True, default='', max_length=100, verbose_name='parameter')),
                ('ins', models.TextField(default='', max_length=1000, verbose_name='seeddir')),
                ('inputCommand', models.TextField(blank=True, default='', max_length=500, verbose_name='inputCommand')),
                ('inputFile', models.CharField(max_length=50, verbose_name='inputFile')),
            ],
        ),
        migrations.CreateModel(
            name='usedSoft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('version', models.CharField(max_length=50, verbose_name='version')),
                ('timeStamp', models.DateTimeField(verbose_name='timeStamp')),
            ],
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
