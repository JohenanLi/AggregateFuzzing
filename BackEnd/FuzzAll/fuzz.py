from Util.decompress import cd, mymkdir, pathJoin, pwd
import sys
import os
import subprocess
from FuzzAll import check, config
from FuzzAll.compileDeal import compile
from .config import AFL_PATH, COLL_PATH, MEM_AFL_PATH,ANDAND, TORTOISE_PATH
import re
from crontab import CronTab
# from croniter import croniter
from datetime import datetime,timedelta
from re import match
"""
    fuzzer ==> fuzzer's name
    compiled pragram's path
    if pragram has been re-compiled with fuzz-tools isqemu = 0; otherwise 1
    ins ==> init_seed 's dir
    outs ==> fuzz_tools's out dir
    pragrams' prePara
    isfile ==> if file read from file
"""
ALL_PATHS = {'MEM': pathJoin(MEM_AFL_PATH),
             "AFL": pathJoin(AFL_PATH),
             "COLL": pathJoin(COLL_PATH),
             "TORTOISE": pathJoin(TORTOISE_PATH)}
DIRS = {
    'MEM_PATH': "/root/fuzzResult/memaflDir",
    "AFL_PATH": "/root/fuzzResult/aflDir",
    "COLL_PATH": "/root/fuzzResult/collaflDir",
    "TORTOISE_PATH": "/root/fuzzResult/tortoiseDir"
}

def fuzz_one(fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute):

    if isqemu:
        qemu = '-Q'
    else:
        qemu = ""
    fuzz_cmd = None
    terminalName: str = programName
    print("fuzzing过程")
    if fuzzer == "afl":
        afl = pathJoin(config.AFL_PATH, "afl-fuzz")
        result = compile(program_path, compileCommand, config.AFL_PATH,1)
        subprocess.Popen("mkdir -p %s" % (outs), shell=True)
        findCmd = ["cd",program_path,ANDAND,"find",".","-type","f","-executable","|","grep","-E","\"%s?[^\.]$\""] %(programName)
        print(findCmd)
        programName = subprocess.getoutput(findCmd)
        print(programName)
        fuzz_cmd = [afl, qemu, "-M master -m 1000", "-i", ins, "-o", outs,
                    "--", program_path, "/", programName, "", prePara, "@@"]

    elif fuzzer == "tortoise":
        tortoise = pathJoin(config.TORTOISE_PATH, "bb_metric", "afl-fuzz")
        result = compile(program_path, compileCommand, config.TORTOISE_PATH,2)
        subprocess.Popen("mkdir -p %s" % (outs), shell=True)
        findCmd = "cd %s && find . -type f -executable | grep -E \"%s?[^\.]$\" " % (
            program_path, programName)
        print(findCmd)
        programName = subprocess.getoutput(findCmd)
        print(programName)
        fuzz_cmd = [tortoise, qemu, "-i ", ins, " -o ", outs,
                    " -- ", program_path, "/", programName, " ", prePara, " @@"]

    elif fuzzer == "mem":
        mem = pathJoin(MEM_AFL_PATH, "mm_metric", "afl-fuzz")
        result = compile(program_path, compileCommand, MEM_AFL_PATH,2)
        mymkdir(outs)
        
        findCmd = ["find",program_path,"-type","f","-executable"]
        regex = "%s?[^\.]$"%(programName)
        with subprocess.Popen(findCmd,stdout=subprocess.PIPE,universal_newlines=True) as process:
            for line in process.stdout:
                if(re.search(regex,line)):
                    
                    programName = line.rstrip()
                    break
        fuzz_cmd = [mem, qemu, "-i", ins, "-o", outs,"--",programName,prePara,"@@",postPara]
    else:
        print("error fuzzer: {}".format(fuzzer))

    # if isfile:                  ## read from file
    #     fuzz_cmd.append(" @@")
    # else:
    #     pass
    cpuResult = subprocess.getoutput(pathJoin(MEM_AFL_PATH,"afl-gotcpu"))
    regexExp = "AVAILABLE"
    availCPU = cpuResult.count(regexExp)#可以用cpu数量获取

    fuzz_cmd = ["tmux","new-session","-s",terminalName,"-d"] + fuzz_cmd
    temp = ""
    for onePara in fuzz_cmd:
        temp = temp + " " + onePara
    fuzz_cmd = temp
    root_dir = pwd()
    cd(outs)
    subprocess.run(temp,shell = True)
    cd(root_dir)
    cron = CronTab(user="root")
    job = cron.new("python3 /root/AggregateFuzzing/BackEnd/Util/joblist.py -d %s"%(outs),"可能删除产生的多余文件")
    job.minute.on(10)

    #cronjob时间生成
    stopJob = cron.new("tmux kill-session -t %s"%(programName),"停止fuzz")
    str_time_now=datetime.now() + timedelta(0.0,0.0,0.0,0.0,float(minute),float(hour),0.0)
    print(str_time_now.minute,str_time_now.hour,str_time_now.day,str_time_now.month,(str_time_now.weekday() + 1)%7)
    stopJob.setall(str_time_now.minute,str_time_now.hour,str_time_now.day,str_time_now.month,(str_time_now.weekday()+1)%7)
    cron.write()
    # iter=croniter("0 8 * * *",str_time_now)

    # print(iter.get_next(datetime))

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Path_Build():
    
    def __init__(self,fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute) -> None:
        self.program_path = program_path
        self.fuzzer_path = ALL_PATHS[fuzzer.upper()]
        self.fuzzer = fuzzer.upper()
        self.programName = programName
        self.prePara = prePara
        self.postPara = postPara
        self.isfile = isfile
        self.compileCommand = compileCommand
        self.hour = hour
        self.minute = minute
        self.ins = ins
        self.outs = outs
        self.isqemu = isqemu
    def compile(self):
        code = -1
        if self.fuzzer == "MEM" or self.fuzzer == "TORTOISE":
            code = 2
        elif self.fuzzer == "AFL" or self.fuzzer == "COLL":
            code = 1
        result = compile(self.program_path, self.compileCommand, self.fuzzer_path,code)
        mymkdir(self.outs)

    def create(self, core: int, isfile=1,dev=0):
        # findCmd = ["find",self.program_path,"-type","f","-executable"]
        # regex = "%s?[^\.]$"%(self.programName)
        # with subprocess.Popen(findCmd,stdout=subprocess.PIPE,universal_newlines=True) as process:
        #     for line in process.stdout:
        #         if(re.search(regex,line)):
                    
        #             self.programName = line.rstrip()
        #             break
        qemu = ""
        if self.isqemu:
            qemu = "-Q"
        else:
            pass
        identity = ""
        master = " -M master -m 1000 "
        slave = "-S slave"
        if self.fuzzer == "TORTOISE":
            afl = self.fuzzer_path + "/bb_metric/afl-fuzz"
        else:
            afl = self.fuzzer_path + "/afl-fuzz"

        for i in range(core):
            if i == 0:
                identity = master
            else:
                identity = slave + str(i) + " -m 1000 "
            fuzz_cmd = ["tmux","new-session","-s",self.programName+str(i),"-d",afl, qemu, identity, "-i", self.ins, "-o", self.outs,"--", self.program_path, self.prePara]
            if isfile:
                fuzz_cmd.append("@@")
            else:
                pass
            if self.postPara:
                fuzz_cmd.append(self.postPara)
            else:
                pass
            runCMD = " ".join(fuzz_cmd)
            print(runCMD)
if __name__ == '__main__':
    print(config.MAX_TIMES)
