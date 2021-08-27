import gdb
import os
import sys


class SelectUniqueCorpus(gdb.Command):


	def __init__(self):
		super(self.__class__, self).__init__("gdb_info", gdb.COMMAND_USER)


	def invoke(self,):
		dir = ""
		with open("/root/AggregateFuzzing/BackEnd/Util/dir.txt","r") as f:
			dir = f.readline()
			f.close()
		
		gdb_info_path = os.path.join(dir,"gdb_info")
		dir_res = os.listdir(dir)
		for one_dir in dir_res:
			try:
				with open(os.path.join(dir,one_dir,"fuzzer_stats"),"r") as f:
					lines = f.readlines()
					f.close()
				cmd  = (lines[-1].split("-- "))[1].rstrip()
				cmd = cmd.split(" ")
				print(cmd)
				crashes = os.listdir(os.path.join(dir,one_dir,"crashes"))
				if not os.path.isdir(os.path.join(gdb_info_path,one_dir)):
					os.makedirs(os.path.join(gdb_info_path,one_dir))
				for crash in crashes:
					start = gdb.execute("file "+cmd[0],to_string = True)
					print(crash)
					runCmd = "r {} {} {}".format(cmd[1], os.path.join(dir,one_dir,"crashes",crash), cmd[3])
					reback = gdb.execute(runCmd, to_string = True)
					btrace = gdb.execute("bt 10", to_string = True)
					# traces = btrace.split('\n')[:-1]
					
					with open(os.path.join(gdb_info_path,one_dir,crash[:9])+".txt","w") as f:
						f.writelines(btrace)
						f.close()
				
					
			except Exception as e:
				print(e)
			# for i in range(len(root_res)):
			# 	for crash in crash_stats[i]:
			# 		temp_replace = os.path.join(root_res[i],"crashes",crash)
			# 		status_res.append( (getstatusoutput(cmd.replace("@@",temp_replace)))[0] )
		quit = gdb.execute("quit", to_string = True)
        # for root in root_res:
        #     crash = os.listdir(os.path.join(root,"crashes"))
        #     crash_stats.append(crash)
a = SelectUniqueCorpus()
a.invoke()