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

def fuzz_one(fuzzer, program_path, isqemu, ins, outs, params, isfile):
    if isqemu:
        qemu = '-Q'
    else:
        qemu = " "
    fuzz_cmd = none

    if fuzzer == "afl":
        afl = os.path.join(config.AFL_PATH, "afl-fuzz")
        fuzz_cmd = [afl, qemu, "-i", ins, "-o", outs, "--", program_path, params]
    elif fuzzer == "tortoise":
        tortoise = os.path.join(config.AFL_PATH, "bb_metric", "afl-fuzz")
        fuzz_cmd = [tortoise, qemu, "-i", ins, "-o", outs, "--", program_path, params]

    elif fuzzer == "emem":
        emem = os.path.join(config.AFL_PATH, "mem_metric", "afl-fuzz")
        fuzz_cmd = [emem, qemu, "-i", ins, "-o", outs, "--", program_path, params]
    else:
        print("error fuzzer: {}".format(fuzzer))

    # screen background for fuzz
    fuzz_cmd = ["screen", "-dmS", "fuzz"] + fuzz_cmd
    if isfile:                  ## read from file
        fuzz_cmd.append("@@")
    subprocess.Popen(fuzz_cmd)
    pass

if __name__ == '__main__':
    print(config.MAX_TIMES)