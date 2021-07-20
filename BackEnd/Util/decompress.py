from os import chdir,makedirs,getcwd,path,listdir, remove,system
from shutil import rmtree
from subprocess import getoutput
from FuzzAll.config import MEM_AFL_PATH
import sys
def cd(dir:str):
    chdir(dir)

def pwd():
    return getcwd()

def mymkdir(dir:str):
    if path.exists(dir):
        system("rm -rf %s"%(dir))
    
    makedirs(dir)

def pathJoin(a,*p):
    res = path.join(a,*p)
    return res

def gotcpu():
    cpuResult = getoutput(pathJoin(MEM_AFL_PATH,"afl-gotcpu"))
    regexExp = "AVAILABLE"
    availCPU = cpuResult.count(regexExp)#可以用cpu数量获取
    return availCPU