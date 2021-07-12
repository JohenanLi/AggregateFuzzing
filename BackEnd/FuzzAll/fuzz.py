import sys
import os
import subprocess
from FuzzAll import check, config
from FuzzAll.compileDeal import compile
from . import config
"""
    fuzzer ==> fuzzer's name
    compiled pragram's path
    if pragram has been re-compiled with fuzz-tools isqemu = 0; otherwise 1
    ins ==> init_seed 's dir
    outs ==> fuzz_tools's out dir
    pragrams' params
    isfile ==> if file read from file
"""


def fuzz_one(fuzzer, program_path, isqemu, ins, outs, params, isfile, compileCommand, programName):
    if isqemu:
        qemu = '-Q'
    else:
        qemu = " "
    fuzz_cmd = None
    terminalName: str = programName

    if fuzzer == "afl":
        afl = os.path.join(config.AFL_PATH, "afl-fuzz")
        result = compile(program_path, compileCommand, config.AFL_PATH)
        subprocess.Popen("mkdir -p %s" % (outs), shell=True)
        findCmd = "cd %s && find . -type f -executable | grep -E \"%s?[^\.]$\" " % (
            program_path, programName)
        print(findCmd)
        programName = subprocess.getoutput(findCmd)
        print(programName)
        fuzz_cmd = [afl, qemu, " -M master -m 1000 ", "-i ", ins, " -o ", outs,
                    " -- ", program_path, "/", programName, " ", params, " @@"]

    elif fuzzer == "tortoise":
        tortoise = os.path.join(config.TORTOISE_PATH, "bb_metric", "afl-fuzz")
        result = compile(program_path, compileCommand, config.TORTOISE_PATH)
        subprocess.Popen("mkdir -p %s" % (outs), shell=True)
        findCmd = "cd %s && find . -type f -executable | grep -E \"%s?[^\.]$\" " % (
            program_path, programName)
        print(findCmd)
        programName = subprocess.getoutput(findCmd)
        print(programName)
        fuzz_cmd = [tortoise, qemu, "-i ", ins, " -o ", outs,
                    " -- ", program_path, "/", programName, " ", params, " @@"]

    elif fuzzer == "mem":
        emem = os.path.join(config.EMEM_AFL_PATH, "mem_metric", "afl-fuzz")
        result = compile(program_path, compileCommand, MEM_AFL_PATH)
        subprocess.Popen("mkdir -p %s" % (outs), shell=True)
        findCmd = "cd %s && find . -type f -executable | grep -E \"%s?[^\.]$\" " % (
            program_path, programName)
        print(findCmd)
        programName = subprocess.getoutput(findCmd)
        print(programName)
        fuzz_cmd = [emem, qemu, "-i ", ins, " -o ", outs,
                    " -- ", program_path, "/", programName, " ", params, " @@"]
    else:
        print("error fuzzer: {}".format(fuzzer))

    # if isfile:                  ## read from file
    #     fuzz_cmd.append(" @@")
    # else:
    #     pass

    fuzz_cmd = ["tmux new -s ", terminalName, " -d "] + fuzz_cmd
    print(fuzz_cmd)
    # subprocess.Popen(fuzz_cmd)
    sysCmd = ''
    sysCmd = sysCmd.join(fuzz_cmd)
    print(sysCmd)
    subprocess.Popen(sysCmd, shell=True)
    # print(sysCmd)
    # os.system(sysCmd)
    # pass


if __name__ == '__main__':
    print(config.MAX_TIMES)
