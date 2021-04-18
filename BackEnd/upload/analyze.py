from BackEnd.settings import SOURCE_FILE_PATH
from os import system
class Analyze():
    """
    tar.gz / zip 解压并返回路径
    """
    def __init__(self,file) -> None:
        self.file = file
        self.filePath = file.split(".")[0]
        return None
    def Unzip(self):
        if "tar.gz" or "tar.xz" in self.file:
            self.filePath = self.file.split(".tar")[0]
            # system("mkdir "+self.filePath)
            myCmd = "cd %s && " %(SOURCE_FILE_PATH)
            myCmd += "tar -xf %s" %(self.file)
            
            system(myCmd)
            return self.filePath
        elif "zip" in self.file:
            myCmd = "unzip %s" %(self.file)
            return self.filePath
        else:
            print("Please wait!!!!")
            return 0