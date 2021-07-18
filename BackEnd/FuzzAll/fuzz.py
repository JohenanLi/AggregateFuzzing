from Util.decompress import cd, mymkdir, pathJoin, pwd,delDuplicate
import sys
import os
import subprocess
from FuzzAll import check, config
from FuzzAll.compileDeal import compile
from . import config
from .config import MEM_AFL_PATH,ANDAND
import re
from crontab import CronTab
"""
    fuzzer ==> fuzzer's name
    compiled pragram's path
    if pragram has been re-compiled with fuzz-tools isqemu = 0; otherwise 1
    ins ==> init_seed 's dir
    outs ==> fuzz_tools's out dir
    pragrams' prePara
    isfile ==> if file read from file
"""


def fuzz_one(fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName):
   
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
        # findCmd = "cd %s && find . -type f -executable | grep -E \"%s?[^\.]$\" " % (
        #     program_path, programName)
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
    job = cron.new(delDuplicate(outs),"可能删除可能产生的多余文件")
    job.minute.on(10)
    cron.write()
    return 


if __name__ == '__main__':
    print(config.MAX_TIMES)
