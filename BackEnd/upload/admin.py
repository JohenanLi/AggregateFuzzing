from django.contrib import admin
from .models import uploadSourceCode,codeResult,uploadSourceProgram,programResult
# Register your models here.
class UploadSourceAdmin(admin.ModelAdmin):

    #显示的列
    list_display = ['id','filePath','name','ins','inputFile','compileCommand','prePara','postPara','inputCommand']
    search_fields =  ['id','filePath','name','ins','inputFile','compileCommand','prePara','postPara','inputCommand']
    list_filter =  ['id','filePath','name','ins','inputFile','compileCommand','prePara','postPara','inputCommand']
    list_editable =  ['filePath','name','ins','inputFile','compileCommand','prePara','postPara','inputCommand']

class CodeResultAdmin(admin.ModelAdmin):

    #显示的列
    list_display = ['id','programName','fuzzer','codeCoverage','crashes','time','code']
    search_fields =  ['id','programName','fuzzer','codeCoverage','crashes','time','code']
    list_filter =  ['id','programName','fuzzer','codeCoverage','crashes','time','code']
    list_editable =  ['programName','fuzzer','codeCoverage','crashes','time','code']
admin.site.register(uploadSourceCode,UploadSourceAdmin)
admin.site.register(codeResult,CodeResultAdmin)
admin.site.register(uploadSourceProgram)
admin.site.register(programResult)