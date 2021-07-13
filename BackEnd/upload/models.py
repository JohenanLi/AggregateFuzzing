from django.db import models
from django.db.models.deletion import CASCADE
import os
# Create your models here.


class uploadSourceCode(models.Model):
    id = models.AutoField('id', primary_key=True)
    filePath = models.TextField(
        'filePath', max_length=500)  # program'path
    name = models.CharField('name', max_length=100)  # fuzzer'name
    ins = models.TextField('seeddir', max_length=500, default='', null=True)
    inputFile = models.CharField('inputFile', max_length=500,null=True)
    compileCommand = models.CharField(
        'compileCommand', max_length=100, default='')
    parameter = models.CharField(
        'parameter', max_length=100, default='', blank=True)
    inputCommand = models.TextField(
        'inputCommand', max_length=500, default='', blank=True)

    def __str__(self):
        return self.name


class uploadSourceProgram(models.Model):
    id = models.AutoField('id', primary_key=True)
    filePath = models.CharField('filePath',max_length=50)
    name = models.CharField('name', max_length=100, default='')
    parameter = models.CharField(
        'parameter', max_length=100, default='', blank=True)

    ins = models.TextField('seeddir', max_length=1000, default='')
    inputCommand = models.TextField(
        'inputCommand', max_length=500, default='', blank=True)
    inputFile = models.CharField('inputFile',max_length=50)

    def __str__(self):
        return self.name


class codeResult(models.Model):
    id = models.AutoField('id', primary_key=True)
    codeCoverage = models.CharField('codeCoverage', max_length=10)
    bugs = models.TextField('bugs', max_length=1000)
    sample = models.CharField('sample', max_length=100)
    code = models.OneToOneField(to=uploadSourceCode, on_delete=CASCADE)


class programResult(models.Model):
    id = models.AutoField('id', primary_key=True)
    codeCoverage = models.CharField('codeCoverage', max_length=10)
    bugs = models.TextField('bugs', max_length=1000)
    sample = models.CharField('sample', max_length=100)
    program = models.OneToOneField(to=uploadSourceProgram, on_delete=CASCADE)


class usedSoft(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("name", max_length=100)
    version = models.CharField("version", max_length=50)
    timeStamp = models.DateTimeField("timeStamp")
