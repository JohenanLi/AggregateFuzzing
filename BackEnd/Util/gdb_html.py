from jinja2 import Environment, FileSystemLoader
import os
from os import getcwd
import subprocess

# __file__ 就是本文件的名字
# 得到放置模板的目录
# path = '{}/templates/'.format(os.path.dirname(__file__))
dir = os.path.join("/root/fuzzResult","MEMAFL","pdftopng")
# with open("/root/AggregateFuzzing/BackEnd/Util/dir.txt","w") as f:
#     f.write(dir)
#     f.close()

# subprocess.run("gdb -q -x /root/AggregateFuzzing/BackEnd/Util/new_gdb_info.py",shell=True)
gdb_info_lines = []
traceUtils = []
for root,dirs,files in os.walk(dir):
    if "gdb_info" in root and dirs == []:
        for file in files:
            f = open(os.path.join(root,file),"r")
            temp = os.path.join(root,file) +"<br>"
            lines = f.readlines()
            temp_tuple = [trace.split(' ')[2] for trace in lines[:-1]]
            
            if temp_tuple not in traceUtils:
                print(temp_tuple,traceUtils)
                traceUtils.append(temp_tuple)
                
                temp += "".join(lines)
                

                temp = temp.replace("\n","<br>")
                gdb_info_lines.append(temp)
            f.close()
print(traceUtils)
path = getcwd()
# 创建一个加载器, jinja2 会从这个目录中加载模板
loader = FileSystemLoader(path)

# 用加载器创建一个环境, 有了它才能读取模板文件
env = Environment(loader=loader)

# 调用 get_template() 方法加载模板并返回
template = env.get_template('demo.html')

# 用 render() 方法渲染模板
# 可以传递参数

a = template.render(gdb_info = gdb_info_lines,bug=len(gdb_info_lines))
with open("res.html","w") as f:
    f.write(a)
    f.close()