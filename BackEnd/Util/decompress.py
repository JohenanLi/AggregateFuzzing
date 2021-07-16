from os import chdir,makedirs,getcwd,path
def cd(dir:str):
    chdir(dir)

def pwd():
    return getcwd()

def mymkdir(dir:str):
    if path.exists(dir):
        pass
    else:
        makedirs(dir)

def pathJoin(a,*p):
    res = path.join(a,*p)
    return res