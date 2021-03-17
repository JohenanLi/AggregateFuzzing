import sys
import os
import subprocess
from FuzzAll import check,config


"""
    fuzzer ==> fuzzer's name
    compiled pragram's path
    if pragram has been re-compiled with fuzz-tools isqemu = 0; otherwise 1
    ins ==> init_seed 's dir
    outs ==> fuzz_tools's out dir
    pragrams' params
    isfile ==> if file read from file
"""

def fuzz_one(fuzzer, program_path, isqemu, ins, outs, params, isfile,compileCommand):
    if isqemu:
        qemu = '-Q'
    else:
        qemu = " "
    fuzz_cmd = None

    if fuzzer == "afl":
        # afl = os.path.join(config.AFL_PATH, "afl-fuzz")
        if compileCommand != '':
            
            new = program_path.split('.')
            cmCmd = compileCommand + ' -o ' + new[0] +'.out'+' ' + program_path 
            print(cmCmd)
            os.system(cmCmd)
            program_path = new[0] +'.out'
            print(program_path)
        fuzz_cmd = ['afl-fuzz', qemu, "-i ", ins, " -o ", outs, " -- ", program_path, params]
    elif fuzzer == "tortoise":
        tortoise = os.path.join(config.AFL_PATH, "bb_metric", "afl-fuzz")
        fuzz_cmd = [tortoise, qemu, "-i", ins, "-o", outs, "--", program_path, params]

    elif fuzzer == "emem":
        emem = os.path.join(config.AFL_PATH, "mem_metric", "afl-fuzz")
        fuzz_cmd = [emem, qemu, "-i", ins, "-o", outs, "--", program_path, params]
    else:
        print("error fuzzer: {}".format(fuzzer))

    
    if isfile:                  ## read from file
        fuzz_cmd.append(" @@")
    else:
        pass
    # screen background for fuzz
    fuzz_cmd = ["screen", "-dmS", "fuzz"] + fuzz_cmd
    print(fuzz_cmd)
    # subprocess.Popen(fuzz_cmd)
    sysCmd = ''
    sysCmd = sysCmd.join(fuzz_cmd)
    subprocess.Popen(sysCmd,shell=False)
    # print(sysCmd)
    # os.system(sysCmd)
    # pass

if __name__ == '__main__':
    print(config.MAX_TIMES)