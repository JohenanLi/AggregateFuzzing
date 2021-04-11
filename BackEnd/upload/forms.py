from django import forms

class sourceCodeForm(forms.Form):
    filePath = forms.CharField()
    name = forms.CharField('name', max_length=100)  # fuzzer'name
    ins = forms.CharField('seeddir', max_length=500,default='',null=True)
    inputFile = forms.CharField('inputFile')
    compileCommand = forms.CharField(
        'compileCommand', max_length=100, default='')
    parameter = forms.CharField('parameter', max_length=100, default='',blank=True)
    inputCommand = forms.CharField('inputCommand', max_length=500, default='',blank=True)