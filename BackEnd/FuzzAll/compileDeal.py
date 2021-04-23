
import sys
import subprocess


def unpack():
    pass


def compile(program_path, compileCommand, fuzzer_path):
    print(program_path, compileCommand, fuzzer_path)
    if "llvm" == compileCommand:
        myCmd = "cd %s &&CC=%s/afl-clang-fast CXX=%s/afl-clang-fast++ ./configure && make && make check" % (
            program_path, fuzzer_path, fuzzer_path)
        print(myCmd)
        subprocess.run(myCmd, shell=True)
    elif "cmake" == compileCommand:
        myCmd = "cd %s && mkdir -p build && cd build && cmake -DCMAKE_CXX_COMPILER=%s/afl-clang-fast++ .. && make && make check" % (
            program_path, fuzzer_path)
        print(myCmd)
        subprocess.run(myCmd, shell=True)


if __name__ == '__main__':

    pass
