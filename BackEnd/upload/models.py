from django.db import models

# Create your models here.


class uploadSourceCode(models.Model):
    id = models.AutoField('id', primary_key=True)
    filePath = models.FileField('filePath', upload_to='sourceCodeFiles/')
    name = models.CharField('name', max_length=100)
    parameter = models.CharField('parameter', max_length=100)

    def __str__(self):
        return self.name


class uploadSourceProgram(models.Model):
    id = models.AutoField('id', primary_key=True)
    filePath = models.FileField('filePath', upload_to='sourceProgramFiles/')
    name = models.CharField('name', max_length=100)
    parameter = models.CharField('parameter', max_length=100)
    compileCommand = models.CharField('compileCommand', max_length=100)

    def __str__(self):
        return self.name
