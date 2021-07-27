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
    prePara = models.CharField(
        'prePara', max_length=100, default='', blank=True)
    postPara = models.CharField(
        'postPara', max_length=100, default='', blank=True)
    inputCommand = models.TextField(
        'inputCommand', max_length=500, default='', blank=True)
    minute = models.CharField(
        'minute', max_length=4, default='', blank=True)
    hour = models.CharField(
        "hour",max_length=3,default="",blank=True)
    # convert @@@ -resize 200% safsadf.png类似于这样的
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
    programName = models.CharField("programName",max_length=100,default="")
    codeCoverage = models.CharField('codeCoverage', max_length=10)
    crashes = models.CharField('crashes', max_length=10,default="0")
    fuzzer = models.CharField('fuzzer', max_length=20,default="")
    time = models.CharField("time",max_length=12,default="")
    code = models.OneToOneField(to=uploadSourceCode, on_delete=CASCADE)


class programResult(models.Model):
    id = models.AutoField('id', primary_key=True)
    codeCoverage = models.CharField('codeCoverage', max_length=10)
    crashes = models.CharField('crashes', max_length=10,default="0")
    fuzzer = models.CharField('fuzzer', max_length=20,default="")
    time = models.CharField("time",max_length=12,default="")
    program = models.OneToOneField(to=uploadSourceProgram, on_delete=CASCADE)


class usedSoft(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("name", max_length=100)
    version = models.CharField("version", max_length=50)
    timeStamp = models.DateTimeField("timeStamp")
