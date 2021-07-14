
from Util.decompress import cd,pwd
import subprocess
import os.path

def unpack():
    pass


def compile(program_path, compileCommand, fuzzer_path,code):
    clang = "afl-clang-fast"
    if code == 2:
        clang = "afl-clang"
    print(program_path, compileCommand, fuzzer_path)
    if "llvm" == compileCommand:
        root_dir = pwd()
        cd(program_path)
        
        myCmd = ["./configure","CC="+os.path.join(fuzzer_path,clang),"CXX="+os.path.join(fuzzer_path,clang+"++")]
        
        # print(program_path)
        # print(myCmd)
        # input()
        #pipe = ,stdout=subprocess.PIPE,stderr=subprocess.PIPE
        p1 = subprocess.call(myCmd)
        p2 = subprocess.call(["make","-j10"])
        cd(root_dir)
        print("编译过程已完成")
    elif "cmake" == compileCommand:
        myCmd = "cd %s && mkdir -p build && cd build && cmake -DCMAKE_CXX_COMPILER=%s/afl-clang-fast++ .. && make -j10" % (
            program_path, fuzzer_path)
        print(myCmd)
        subprocess.run(myCmd)


if __name__ == '__main__':

    pass
