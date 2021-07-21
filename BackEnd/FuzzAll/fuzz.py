from Util.decompress import cd, gotcpu, mymkdir, pathJoin, pwd
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
import _thread
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
        subprocess.run("rm -rf %s"%(self.outs),shell=True)

    def create(self, core: int, isfile=1):
        findCmd = ["find",self.program_path,"-type","f","-executable"]
        regex = "%s?[^\.]$"%(self.programName)
        with subprocess.Popen(findCmd,stdout=subprocess.PIPE,universal_newlines=True) as process:
            for line in process.stdout:
                if(re.search(regex,line)):
                    
                    self.programName = line.rstrip()
                    break
        qemu = ""
        if self.isqemu:
            qemu = "-Q"
        else:
            pass
        identity = ""
        master = "-M master"
        slave = "-S slave"
        if self.fuzzer == "TORTOISE":
            afl = self.fuzzer_path + "/bb_metric/afl-fuzz"
        else:
            afl = self.fuzzer_path + "/afl-fuzz"

        cron = CronTab(user="root")
        root_dir = pwd()
        mymkdir(self.outs)
        cd(self.outs)
        for i in range(core):
            if i == 0:
                identity = master
            else:
                identity = slave + str(i) 
            fuzz_cmd = ["tmux","new-session","-s",str(i)+self.programName.split('/')[-1],"-d",afl, qemu, identity, "-i", self.ins, "-o", self.outs,"--", self.programName, self.prePara]
            #"-t",self.programName.split('/')[-1]+str(i),
            if isfile:
                fuzz_cmd.append("@@")
            else:
                pass
            if self.postPara:
                fuzz_cmd.append(self.postPara)
            else:
                pass
            runCMD = " ".join(fuzz_cmd)
            
            # _thread.start_new_thread(threadUse,(runCMD))
            os.system(runCMD)
            print(runCMD)
            stopJob = cron.new("tmux kill-session -t %s"%(str(i)+self.programName.split('/')[-1]),"停止fuzz")
            str_time_now=datetime.now() + timedelta(0.0,0.0,0.0,0.0,float(self.minute),float(self.hour),0.0)
            stopJob.setall(str_time_now.minute,str_time_now.hour,str_time_now.day,str_time_now.month,(str_time_now.weekday()+1)%7)
        cd(root_dir)
        job = cron.new("python3 /root/AggregateFuzzing/BackEnd/Util/joblist.py -d %s"%(self.outs),"可能删除产生的多余文件")
        job.minute.on(10)
        cron.write()

def fuzz_one(fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute):
    print("fuzzing过程")
    myFuzz = Path_Build(fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute)
    myFuzz.compile()
    myFuzz.create(gotcpu() - 2)

    # iter=croniter("0 8 * * *",str_time_now)

    # print(iter.get_next(datetime))

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    print(config.MAX_TIMES)

# def threadUse(runCMD):
#     print(runCMD)
#     os.system(runCMD)