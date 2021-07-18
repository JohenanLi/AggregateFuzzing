from os import chdir,makedirs,getcwd,path
from shutil import rmtree
def cd(dir:str):
    chdir(dir)

def pwd():
    return getcwd()

def mymkdir(dir:str):
    if path.exists(dir):
        rmtree(dir)
        pass
    
    makedirs(dir)

def pathJoin(a,*p):
    res = path.join(a,*p)
    return res