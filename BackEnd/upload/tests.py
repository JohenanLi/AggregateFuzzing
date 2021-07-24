MEM_AFL_PATH = "/root/AggregateFuzzing/BackEnd/tools/memAfl"
import os
from subprocess import getoutput
whatsup_individual = os.path.join(MEM_AFL_PATH,"afl-whatsup_individual")
whatsup_summary = os.path.join(MEM_AFL_PATH,"afl-whatsup_summary")
outs = os.path.join("/root/fuzzResult","mem","pdftopng")
mem_result_individual = getoutput(whatsup_individual+" "+outs)
mem_result_summary = getoutput(whatsup_summary+" "+outs)
with open("individula.txt","w")as f:
    f.writelines(mem_result_individual)
    f.close()
with open("summary.txt","w")as f:
    f.writelines(mem_result_summary)
    f.close()
# Create your tests here.

