from subprocess import getstatusoutput
import os

from django.http.response import JsonResponse
crash_type = {
    "-6":"释放后重用",
    "-11":"栈溢出",
    "1":""
}
def crash(dir):
    dir_res = os.walk(dir)
    root_res = []
    fuzzer_stats= []
    crash_stats = []
    lines = []
    status_res = []
    message = ""
    for root,dir,files in dir_res:
        if "crashes" in dir:
            root_res.append(root)
    for root in root_res:
        crash = os.listdir(os.path.join(root,"crashes"))
        crash_stats.append(crash)
    
    with open(os.path.join(root_res[0],"fuzzer_stats"),"r") as f:
        lines = f.readlines()
        f.close()
    cmd  = (lines[-1].split("-- "))[1].rstrip()
    for i in range(len(root_res)):
        for crash in crash_stats[i]:
            temp_replace = os.path.join(root_res[i],"crashes",crash)
            status_res.append( (getstatusoutput(cmd.replace("@@",temp_replace)))[0] )
    status_set = set(status_res)
    for status in status_set:
        message += crash_type[str(status)]+"<br>"
    return JsonResponse(message,safe=False)
    
if __name__ == "__main__":
    print(crash("/root/fuzzResult/DRILLER/pdftopng"))
    print(crash("/root/fuzzResult/MEMAFL/pdftopng"))
    print(crash("/root/fuzzResult/TORTOISE/pdftopng"))

# def crash(dir):
#     dir_res = os.walk(dir)
#     root_res = []
#     fuzzer_stats= []
#     crash_stats = []
#     lines = []
#     status_res = []
#     for root,dir,files in dir_res:
#         if "crashes" in dir:
#             root_res.append(root)
#     for root in root_res:
#         crash = os.listdir(os.path.join(root,"crashes"))
#         crash_stats.append(crash)
    
#     with open(os.path.join(root_res[0],"fuzzer_stats"),"r") as f:
#         lines = f.readlines()
#         f.close()
#     cmd  = (lines[-1].split("-- "))[1].rstrip()
#     for i in range(len(root_res)):
#         for crash in crash_stats[i]:
#             temp_replace = os.path.join(root_res[i],"crashes",crash)
#             status_res.append( (getstatusoutput(cmd.replace("@@",temp_replace)))[0] )
#     return status_res