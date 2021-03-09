from django.db import models

# Create your models here.


class uploadSourceCode(models.Model):
    id = models.AutoField('id', primary_key=True)
    filePath = models.FileField(
        'filePath', upload_to='sourceCodeFiles/')  # program'path
    name = models.CharField('name', max_length=100)  # fuzzer'name
    ins = models.TextField('seeddir', max_length=500)
    inputFile = models.FileField('inputFile', upload_to='inputFile/')
    compileCommand = models.CharField(
        'compileCommand', max_length=100, default='')
    parameter = models.CharField('parameter', max_length=100, default='')
    inputCommand = models.TextField('inputCommand', max_length=500, default='')

    def __str__(self):
        return self.name


class uploadSourceProgram(models.Model):
    id = models.AutoField('id', primary_key=True)
    filePath = models.FileField('filePath', upload_to='sourceProgramFiles/')
    name = models.CharField('name', max_length=100, default='')
    parameter = models.CharField('parameter', max_length=100, default='')

    ins = models.TextField('seeddir', max_length=500)
    inputCommand = models.TextField('inputCommand', max_length=500, default='')
    inputFile = models.FileField('inputFile', upload_to='inputFile/')

    def __str__(self):
        return self.name


class codeResult(models.Model):
    id = models.AutoField('id', primary_key=True)
    codeCoverage = models.CharField('codeCoverage', max_length=10)
    bugs = models.TextField('bugs', max_length=1000)
    sample = models.CharField('sample', max_length=100)


class programResult(models.Model):
    id = models.AutoField('id', primary_key=True)
    codeCoverage = models.CharField('codeCoverage', max_length=10)
    bugs = models.TextField('bugs', max_length=1000)
    sample = models.CharField('sample', max_length=100)
