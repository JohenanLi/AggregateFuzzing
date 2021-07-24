import logging
from Util.decompress import cd, gotcpu, mymkdir, pathJoin, pwd
from subprocess import run,getoutput,PIPE,Popen
from FuzzAll import  config
from FuzzAll.compileDeal import compile
from .config import AFL_PATH, COLL_PATH, MEM_AFL_PATH, TORTOISE_PATH
import re
from crontab import CronTab
from datetime import datetime,timedelta
from re import match
import libtmux
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from upload.models import codeResult, uploadSourceCode
"""
    fuzzer ==> fuzzer's name
    compiled pragram's path
    if pragram has been re-compiled with fuzz-tools isqemu = 0; otherwise 1
    ins ==> init_seed 's dir
    outs ==> fuzz_tools's out dir
    pragrams' prePara
    isfile ==> if file read from file
"""
ALL_PATHS = {'MEM': pathJoin(MEM_AFL_PATH),
             "AFL": pathJoin(AFL_PATH),
             "COLL": pathJoin(COLL_PATH),
             "TORTOISE": pathJoin(TORTOISE_PATH)}
DIRS = {
    'MEM': "/root/fuzzResult/mem",
    "AFL": "/root/fuzzResult/afl",
    "COLL": "/root/fuzzResult/collafl",
    "TORTOISE": "/root/fuzzResult/tortoise"
}
# 1.实例化调度器
scheduler = BackgroundScheduler()

# 2.调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")


class Path_Build():
    
    def __init__(self,fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute,id) -> None:
        self.program_path = program_path
        self.fuzzer_path = ALL_PATHS[fuzzer.upper()]
        self.fuzzer = fuzzer.upper()
        self.programName = programName
        self.prePara = prePara
        self.postPara = postPara
        self.isfile = isfile
        self.compileCommand = compileCommand
        self.hour = hour
        self.minute = minute
        self.ins = ins
        self.outs = outs
        self.isqemu = isqemu
        self.id = id ##uploadSource.id
        self.short_name = self.programName.split('/')[-1]
    def compile(self):
        code = -1
        if self.fuzzer == "MEM" or self.fuzzer == "TORTOISE":
            code = 2
        elif self.fuzzer == "AFL" or self.fuzzer == "COLL":
            code = 1
        result = compile(self.program_path, self.compileCommand, self.fuzzer_path,code)
        run("rm -rf %s"%(self.outs),shell=True)

    def stop_job(self):
    # 这里写你要执行的任务
        stop_cmd = "tmux kill-session -t %s"%(self.short_name)
        run(stop_cmd,shell=True)

    def stop_sche(self,str_time_now):
        scheduler.add_job(self.stop_job, 'date',run_date=str_time_now,id="date_"+self.short_name,replace_existing=True)
    def sync_sche(self,stoptime):
        scheduler.add_job(self.sync_database,"cron",minute="*/2",id="cron_"+self.short_name,replace_existing=True)
        scheduler.add_job(self.stop_sync_sche,"date",run_date=stoptime)
    def stop_sync_sche(self):
        scheduler.remove_job("cron_"+self.short_name)
    def sync_database(self,):
        resList = codeResult.objects.filter(code_id = self.id)
        if len(resList) == 0:
            uploadInstance = uploadSourceCode.objects.get(id = self.id)
            resInstance = codeResult.objects.create(programName = self.short_name,
            codeCoverage = "/",crashes = "0",fuzzer = self.fuzzer,time=datetime.now().strftime("%Y-%m-%d"),code = uploadInstance)
            resInstance.save()
            
        elif len(resList) == 1:
            resInstance = codeResult.objects.get(code_id = self.id)
            outs = pathJoin("/root/fuzzResult",self.fuzzer,self.programName)
            whatsup_summary = pathJoin(MEM_AFL_PATH,"afl-whatsup_summary")
            result_summary = getoutput(whatsup_summary+" "+outs)
            # result_summary.
            resInstance.crashes = str(int(resInstance.crashes) + 1)
            resInstance.save()


    def create(self, core: int, isfile=1):
        findCmd = ["find",self.program_path,"-type","f","-executable"]
        regex = "%s?[^\.]$"%(self.programName)
        with Popen(findCmd,stdout=PIPE,universal_newlines=True) as process:
            for line in process.stdout:
                if(re.search(regex,line)):
                    
                    self.programName = line.rstrip()
                    break
        qemu = ""
        if self.isqemu:
            qemu = "-Q"
        else:
            pass
        identity = ""
        master = "-M master -m 1000"
        slave = "-S slave"
        if self.fuzzer == "TORTOISE":
            afl = self.fuzzer_path + "/bb_metric/afl-fuzz"
        else:
            afl = self.fuzzer_path + "/afl-fuzz"

        cron = CronTab(user="root")
        root_dir = pwd()
        mymkdir(self.outs)
        cd(self.outs)
        server = libtmux.Server()
        run(" ".join(["tmux new-session -s", self.short_name, "-d"]),shell=True)
        session = server.find_where({ "session_name": self.short_name })
        for i in range(core):
            if i == 0:
                identity = master
            else:
                identity = slave + str(i) + " -m 1000"
            fuzz_cmd = [afl, qemu, identity,"-i", self.ins, "-o", self.outs,"--", self.programName, self.prePara]
            if isfile:
                fuzz_cmd.append("@@")
            else:
                pass
            if self.postPara:
                fuzz_cmd.append(self.postPara)
            else:
                pass
            runCMD = " ".join(fuzz_cmd)
            w = session.new_window(attach = False,window_name = str(i)+self.short_name)
            pane = w.split_window(attach=False)
            pane.send_keys(runCMD)
            
        # stopJob = cron.new("tmux kill-session -t %s"%(self.short_name),"停止fuzz")
        str_time_now=datetime.now() + timedelta(0.0,0.0,0.0,0.0,float(self.minute),float(self.hour),0.0)
        logging.basicConfig(level=logging.INFO,
                         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S',
                        filename='log1.txt',
                        filemode='a')
        self.stop_sche(str_time_now)
        self.sync_sche(str_time_now)

        scheduler._logger = logging
        scheduler.start()

        cd(root_dir)
        job = cron.new("python3 /root/AggregateFuzzing/BackEnd/Util/joblist.py -d %s"%(self.outs),"可能删除产生的多余文件")
        job.setall("*/10","*","*","*","*")
        cron.write()
        return str_time_now

def fuzz_one(fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute,id):

    
    try:
        print("fuzzing过程")
        myFuzz = Path_Build(fuzzer, program_path, isqemu, ins, outs, prePara, postPara , isfile, compileCommand, programName,hour,minute,id)
        myFuzz.compile()
        tempTime = myFuzz.create(gotcpu() - 2).strftime("%Y-%m-%d %H:%M:%S")
        
        scheduler.print_jobs(DjangoJobStore())
        scheduler.start()
    except Exception as e:
        print(e)
        # 有错误就停止定时器
        scheduler.shutdown()
    

    
    return tempTime #保证服务器正常使用的两个cpu，以及时间返回处理后的时间




if __name__ == '__main__':
    print(config.MAX_TIMES)

