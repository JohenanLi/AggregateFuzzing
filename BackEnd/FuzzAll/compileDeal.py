
import sys
from os import system


def unpack():
    pass

def compile(program_path,compileCommand,fuzzer_path):
    print(program_path,compileCommand,fuzzer_path)
    if "llvm" in compileCommand:
        myCmd = "cd %s &&CC=%s/afl-clang-fast CXX=%s/afl-clang-fast++ ./configure && make && make check" %(program_path,fuzzer_path,fuzzer_path)
        system(myCmd)
if __name__ == '__main__':
    
    pass