from os import chdir,makedirs,getcwd,path,listdir, remove,system
from shutil import rmtree
from subprocess import getoutput
from FuzzAll.config import MEM_AFL_PATH
import re
def cd(dir:str):
    chdir(dir)

def pwd():
    return getcwd()

def mymkdir(dir:str):
    if path.exists(dir):
        system("rm -rf %s"%(dir))
        print("Tst")
    
    makedirs(dir)

def pathJoin(a,*p):
    res = path.join(a,*p)
    return res

def gotcpu():
    cpuResult = getoutput(pathJoin(MEM_AFL_PATH,"afl-gotcpu"))
    regexExp = "AVAILABLE"
    availCPU = cpuResult.count(regexExp)#可以用cpu数量获取
    return availCPU

def invi_table_data(ind_lines):
    reg = ["","","","","",""]
    reg[0] = r"(?<=cycle ).*?(?=,)"
    reg[1] = r"(?<=speed ).*?(?= execs\/sec)"
    reg[2]  = r"(?<=path ).*?(?=\n)"
    reg[3] = r"(?<=pending ).*?(?=,)"
    reg[4] = r"(?<=coverage ).*?(?=,)"
    reg[5] = r"(?<=count ).*?(?= \()"


    mem = []
    result = []
    for i in range(len(reg)):
        result.append(re.findall(reg[i],ind_lines))
    for i in range(2):
        temp = {}
        temp['core'] = i
        try:
            temp['cycle'] = result[0][i]
        except:
            return -1
        temp['speed'] = result[1][i]
        temp['path'] = result[2][i]
        temp['pending'] = result[3][i]
        temp['coverage'] = result[4][i]
        try:
            temp['crashes'] = result[5][i]
        except:
            temp['crashes'] = 0
        mem.append(temp)
    return mem

def sum_table_data(txt):
    total_reg = []
    total_reg.append(r"(?<=alive : ).*?(?=\n)")
    total_reg.append(r"(?<=time : ).*?(?=\n)")
    total_reg.append(r"(?<=execs : ).*?(?= million)")
    total_reg.append(r"(?<=speed : ).*?(?= execs)")
    total_reg.append(r"(?<=faves, ).*?(?= total)")
    total_reg.append(r"(?<=faves, ).*?(?= total \(on)")
    total_reg.append(r"(?<=Crashes found : ).*?(?= locally unique)")
    mem = []
    result = []
    for i in range(len(total_reg)):
        try:
            result.append(re.search(total_reg[i],txt).group())
        except:
            result.append(0)
    temp = {}
    temp['CPU_all'] = result[0]
    result[1] = result[1].replace("days","天")
    temp['run_time'] = result[1].replace("hours","小时")
    temp['total_execs'] = result[2]
    temp['speed_sum'] = result[3]
    result[4] = result[4]
    temp['pending_sum'] = result[4]
    temp['pending'] = result[5]
    temp['crashes_sum'] = result[6]
    mem.append(temp)
    return mem

