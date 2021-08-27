import os
word ={
    "start_time":"开始时间",
    "last_update":"最后更新时间",
    "fuzzer_pid":"模糊器进程的PID",
    "cycles_done":"队列周期到目前为止已完成",
    "execs_done":"尝试执行execve()的次数",
    "execs_per_sec":"当前每秒的execs数",
    "paths_total":"队列中的条目总数",
    "paths_favored":"依赖条目数",
    "paths_found":"通过本地检测发现的条目数",
    "paths_imported":"从其他实例导入的条目数",
    "max_depth":"生成的数据集中的级别数",
    "cur_path":"当前处理的条目号",
    "pending_favs":"仍在等待模糊处理的首选条目数",
    "pending_total":"等待被模糊处理的所有条目数",
    "variable_paths":"显示变量行为的测试用例数",
    "stability":"行为一致的位图字节的百分比",
    "bitmap_cvg":"位示图覆盖率",
    "unique_crashes":"记录的唯一崩溃次数",
    "unique_hangs":"遇到的唯一挂起次数",
    "last_path": "上次条目产生时间",
    "last_crash": "上次崩溃产生时间",
    "last_hang":"上一次的挂起时间",
    "execs_since_crash":"自从上次崩溃后的执行次数",
    "exec_timeout":"执行超时时间",
    "afl_banner":"执行名称",
    "afl_version":"版本号",
    "target_mode":"目标模式",
    "command_line":"执行命令"
}
def trans(fuzzer_stats):
    lines = []
    with open(fuzzer_stats,"r") as f:
        lines = f.readlines()
        f.close()
    new_lines = []
    for i in range(len(lines)):
        new_lines.append(lines[i].replace(list(word.keys())[i],list(word.values())[i]))
    with open(fuzzer_stats,"w") as f:
        f.writelines(new_lines)
        f.close()
def fuzzer_trans(dir):
    for root, dirs, files in os.walk(dir):
        if "fuzzer_stats" in files :
            trans(os.path.join(root,"fuzzer_stats"))