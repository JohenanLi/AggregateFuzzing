from os import chdir,makedirs,mkdir,getcwd
def cd(dir:str):
    chdir(dir)

def makedirs(dir:str):
    makedirs(dir)

def mkdir(dir:str):
    mkdir(dir)

def pwd():
    return getcwd()