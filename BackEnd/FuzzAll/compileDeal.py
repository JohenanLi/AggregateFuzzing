from Util.decompress import cd,pwd,mymkdir,pathJoin
import subprocess
import os
def unpack():
    pass


def mycompile(program_path, compileCommand, fuzzer_path,code):
    clang = "afl-clang-fast"
    tempClang = "afl-clang-fast++"
    RANLIB = pathJoin("/usr/bin","llvm-ranlib-12")
    AR = pathJoin("/usr/bin","llvm-ar-12")
    makeStart = ["make","-j10"]
    if code == 2:
        # clang = "afl-clang"
        # tempClang = "afl-clang++"
        pass
    elif code == 1:
        clang = "afl-clang"
        tempClang = "afl-clang++"
    elif code == 3:
        clang = "afl-clang-lto"
        tempClang = "afl-clang-lto++"
	
    root_dir = pwd()
    cd("".join([program_path,compileCommand]))
    print(type(subprocess.getoutput('find . -name CMakeLists.txt')))
    
    if subprocess.getoutput('find . -name CMakeLists.txt') == "":



        myCmd = ["".join(["CC=",os.path.join(fuzzer_path,clang)]),
        "".join(["CXX=",os.path.join(fuzzer_path,tempClang)]),"./configure --disable-shared"]
        if code==3:
            myCmd.append("RANLIB="+RANLIB)
            myCmd.append("AR="+AR)
        
        myCmd = " ".join(myCmd)
        print(myCmd)
        p1 = subprocess.run(myCmd,shell=True)
        p2 = subprocess.run(makeStart,shell=True)
        cd(root_dir)
        
    else:
        # myCmd = "cd %s && mkdir -p build && cd build && cmake -DCMAKE_CXX_COMPILER=%s/afl-clang-fast++ .. && make -j10" % (
        #     program_path, fuzzer_path)
        mymkdir("build")
        cd("build")
        print(pwd())
        #-DCMAKE_C_COMPILER=%s pathJoin(fuzzer_path,clang),
        # myCmd =["cmake","-DCMAKE_CXX_COMPILER=%s"%(pathJoin(fuzzer_path,"".join([clang,"++"]))),".."]
        myCmd = "cmake -DCMAKE_C_COMPILER=%s  -DCMAKE_CXX_COMPILER=%s .."%(pathJoin(fuzzer_path,clang),pathJoin(fuzzer_path,tempClang))
        print(myCmd)
        subprocess.run(myCmd,close_fds=True,shell=True)
        subprocess.run(makeStart,close_fds=True)
        cd(root_dir)
        print("编译过程已完成")



if __name__ == '__main__':

    pass
