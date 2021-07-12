from BackEnd.settings import SOURCE_FILE_PATH
from subprocess import run
class Analyze():
    """
    tar.gz / zip 解压并返回路径
    """
    def __init__(self,file:str) -> None:
        self.file = file
        self.filePath = file.split(".")[0]
        return None
    def Unzip(self):
        myCmd = "cd %s && " %(SOURCE_FILE_PATH)
        if self.file.endswith(".gz") or self.file.endswith(".xz") or self.file.endswith("bz2") or self.file.endswith("tar"):
            self.filePath = self.file.split(".tar")[0]
            # system("mkdir "+self.filePath)
            print("Analyze Progess")
            
            myCmd += "tar -xvf %s" %(self.file)
            try:
                run(myCmd)
            except:
                print("文件解压失败")
                return "文件解压失败"
            return self.filePath
        elif self.file.endswith("zip"):
            myCmd += "unzip %s" %(self.file)
            try:
                run(myCmd)
            except:
                print("文件解压失败")
                return "文件解压失败"
            return self.filePath
        elif self.file.endswith("7z"):
            myCmd += "7za x %s -r -o./" %(self.file)
            try:
                run(myCmd)
            except:
                print("文件解压失败")
                return "文件解压失败"
            return self.filePath
        else:
            print("错误，不是压缩文件格式")
            return "错误，不是压缩文件格式"