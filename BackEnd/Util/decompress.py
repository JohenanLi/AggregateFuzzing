from os import chdir,makedirs,getcwd,path,listdir, remove,system
from shutil import rmtree
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

