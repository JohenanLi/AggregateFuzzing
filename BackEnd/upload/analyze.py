from os import makedirs, mkdir
from FuzzAll.config import ANDAND
from BackEnd.settings import SOURCE_FILE_PATH
from subprocess import run, call,run
import traceback,sys,subprocess
from Util.decompress import pwd,cd
class Analyze():
    """
    tar.gz / zip 解压并返回路径
    """
    def __init__(self,file:str) -> None:
        self.file = file
        self.filePath = file.split(".")[0]
        self.programName = self.filePath.split("/")[-1]
        print(self.filePath,self.programName)
        return None
    def Unzip(self):
        root_dir = pwd()
        if self.file.endswith(".gz") or self.file.endswith(".xz") or self.file.endswith("bz2") or self.file.endswith("tar"):
            self.filePath = self.file.split(".tar")[0]
            # system("mkdir "+self.filePath)
            print("Analyze Progess")
            cd(SOURCE_FILE_PATH)
            try:
                makedirs("./%s"%(self.programName))
            except Exception:
                pass
            #myCmd = ['tar','-xvf',self.file,"-C","./%s"%(self.programName)]
            myCmd = ['tar','-xvf',self.file]
            print(myCmd)
            try:
                p1 = call(myCmd)
                cd(root_dir)
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                return "文件解压失败"
            return self.filePath
        elif self.file.endswith("zip"):
            cd(SOURCE_FILE_PATH)
            myCmd = "unzip %s " %(self.file)
            try:
                run(myCmd,shell=True)
                cd(root_dir)
            except:
                print("文件解压失败")
                return "文件解压失败"
            return self.filePath
        elif self.file.endswith("7z"):
            myCmd = "7za x %s -r -o./" %(self.file)
            print(myCmd)
            try:
                run(myCmd,shell=True)
                cd(root_dir)
            except:
                print("文件解压失败")
                return "文件解压失败"
            return self.filePath
        else:
            print("错误，不是压缩文件格式")
            return "错误，不是压缩文件格式"