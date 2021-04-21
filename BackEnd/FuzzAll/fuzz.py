import sys
import os
import subprocess
from FuzzAll import check, config
from FuzzAll.compileDeal import compile
from FuzzAll.config import AFL_PATH
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
    if os.path.isfile(os.path.join(program_path, "/", programName)):
        print("***********************")
    else:
        programName = "/src/" + programName
    if fuzzer == "afl":
        # afl = os.path.join(config.AFL_PATH, "afl-fuzz")
        if compileCommand != '':

            """llvm"""
            result = compile(program_path, compileCommand, AFL_PATH)
        os.system("mkdir %s" % (outs))
        fuzz_cmd = [AFL_PATH, '/afl-fuzz', qemu, "-i ", ins, " -o ", outs,
                    " -- ", program_path, "/", programName, " ", params, " @@"]
# /root/work/AggregateFuzzing/BackEnd/tools/afl/mm_metric/afl-fuzz -i /root/work/AggregateFuzzing/BackEnd/tools/aflGithub/testcases/images/png -o /root/work/fuzz/outs -- ~/work/sam2p-0.49.4/sam2p @@

    elif fuzzer == "tortoise":
        tortoise = os.path.join(config.AFL_PATH, "bb_metric", "afl-fuzz")
        fuzz_cmd = [tortoise, qemu, "-i", ins,
                    "-o", outs, "--", program_path, params]

    elif fuzzer == "emem":
        emem = os.path.join(config.AFL_PATH, "mem_metric", "afl-fuzz")
        fuzz_cmd = [emem, qemu, "-i", ins, "-o",
                    outs, "--", program_path, params]
    else:
        print("error fuzzer: {}".format(fuzzer))

    # if isfile:                  ## read from file
    #     fuzz_cmd.append(" @@")
    # else:
    #     pass
    # screen background for fuzz
    # fuzz_cmd = ["screen", "-dmS", "fuzz"] + fuzz_cmd
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
