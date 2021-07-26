from Util.decompress import cd,pwd,mymkdir,pathJoin
import subprocess

def unpack():
    pass


def compile(program_path, compileCommand, fuzzer_path,code):
    clang = "afl-clang-fast"
    makeStart = ["make","-j10"]
    if code == 2:
        clang = "afl-clang"
    root_dir = pwd()
    cd("".join([program_path,compileCommand]))
    if subprocess.getoutput('find . -name "CMakeLists.txt"') == None:
        myCmd = ["./configure","".join(["CC=",pathJoin(fuzzer_path,clang)]),"".join(["CXX=",pathJoin(fuzzer_path,"".join([clang,"++"]))])]
        
        # print(program_path)
        print(myCmd)
        # input()
        #pipe = ,stdout=subprocess.PIPE,stderr=subprocess.PIPE
        p1 = subprocess.run(myCmd,close_fds=True)
        p2 = subprocess.run(makeStart,close_fds=True)
        cd(root_dir)
        
    else:
        # myCmd = "cd %s && mkdir -p build && cd build && cmake -DCMAKE_CXX_COMPILER=%s/afl-clang-fast++ .. && make -j10" % (
        #     program_path, fuzzer_path)
        mymkdir("build")
        cd("build")
        myCmd =["cmake","-DCMAKE_CXX_COMPILER=%s"%(pathJoin(fuzzer_path,"".join([clang,"++"]))),".."]
        subprocess.run(myCmd,close_fds=True)
        subprocess.run(makeStart,close_fds=True)
        cd(root_dir)
        print("编译过程已完成")


if __name__ == '__main__':

    pass
