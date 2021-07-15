<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card shadow="hover" class="mgb20" style="height: 252px">
          <div class="user-info">
            <img src="../assets/img/img.jpg" class="user-avator" alt />
            <div class="user-info-cont">
              <div class="user-info-name">{{ name }}</div>
              <div>{{ role }}</div>
            </div>
          </div>
          <div class="user-info-list">
            上次登录时间：
            <span>{{ time }}</span>
          </div>
          <div class="user-info-list">
            上次登录地点：
            <span>长沙</span>
          </div>
        </el-card>
        <!-- <el-card shadow="hover"> -->
        <!-- <template #header>
            <div class="clearfix">
              <span>CPU资源详情</span>
            </div>
          </template>
          可用CPU资源
          <el-progress :percentage="avail_cpu" color="#42b983"></el-progress
          >已用CPU资源
          <el-progress :percentage="notavail_cpu" color="#f56c6c"></el-progress> -->
        <!-- </el-card> -->
        <!-- 
        <el-card shadow="hover">
          <template #header>
            <div class="clearfix">
              <span>语言详情</span>
            </div>
          </template>
          Vue
          <el-progress :percentage="71.3" color="#42b983"></el-progress
          >JavaScript
          <el-progress :percentage="24.1" color="#f1e05a"></el-progress>CSS
          <el-progress :percentage="13.7"></el-progress>HTML
          <el-progress :percentage="5.9" color="#f56c6c"></el-progress>
        </el-card>-->
      </el-col>

      <!-- <el-col :span="16">
        <el-row :gutter="25" type="flex" class="row-bg" justify="space-between">
          <el-col :span="16" style="height: 180px">
            <el-card shadow="hover">
              <div class="grid-content grid-con-1">
                <i class="el-icon-document grid-con-icon"></i>
                <div class="grid-cont-right">
                  <el-button type="text" @click="sourceCode()"
                    ><div class="grid-num">上传源代码并编译</div></el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="16" style="height: 180px">
            <el-card shadow="hover">
              <div class="grid-content grid-con-2">
                <i class="el-icon-box grid-con-icon"></i>
                <div class="grid-cont-right">
                  <el-button type="text" @click="sourceProgram()"
                    ><div class="grid-num">上传可执行文件</div></el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>  

          <el-col :span="16" style="height: 180px">
            <el-card shadow="hover">
              <div class="grid-content grid-con-3">
                <i class="el-icon-loading grid-con-icon"></i>
                <div class="grid-cont-right">
                  <el-button type="text" @click="history()"
                    ><div class="grid-num">历史记录</div></el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="16" style="height: 180px">
            <el-table
              :data="tableData"
              style="width: 100%"
            >
              <el-table-column prop="id" label="id" width="180">
              </el-table-column>
              <el-table-column prop="name" label="软件名称" width="180">
              </el-table-column>
              <el-table-column prop="version" label="版本">
              </el-table-column>
              <el-table-column prop="timeStamp" label="测试时间">
              </el-table-column>
            </el-table>
          </el-col>
        </el-row>
      </el-col> -->
    </el-row>
  </div>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column type="expand">
      <template #default="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="programName">
            <span>{{ props.row.programName }}</span>
          </el-form-item>
          <el-form-item label="tool">
            <span>{{ props.row.tool }}</span>
          </el-form-item>
          <el-form-item label="pathCoverage">
            <span>{{ props.row.path_cvg }}</span>
          </el-form-item>
          <el-form-item label="totalCrashes">
            <span>{{ props.row.total_crashes }}</span>
          </el-form-item>
          <el-form-item label="startTime">
            <span>{{ props.row.start_time }}</span>
          </el-form-item>
          <el-form-item label="lastUpdate">
            <span>{{ props.row.last_update }}</span>
          </el-form-item>
          <el-form-item label="queueCycles">
            <span>{{ props.row.cycles_done }}</span>
          </el-form-item>
          <el-form-item label="execveCalls">
            <span>{{ props.row.execs_done }}</span>
          </el-form-item>
          <el-form-item label="execs_per_sec">
            <span>{{ props.row.execs_per_sec }}</span>
          </el-form-item>
          <el-form-item label="totalPaths">
            <span>{{ props.row.paths_total }}</span>
          </el-form-item>
          <el-form-item label="favoredPaths">
            <span>{{ props.row.paths_favored }}</span>
          </el-form-item>
          <el-form-item label="pathsFound">
            <span>{{ props.row.paths_found }}</span>
          </el-form-item>
          <el-form-item label="importedPaths">
            <span>{{ props.row.paths_imported }}</span>
          </el-form-item>
          <el-form-item label="max_depth">
            <span>{{ props.row.max_depth }}</span>
          </el-form-item>
          <el-form-item label="currentPaths">
            <span>{{ props.row.cur_path }}</span>
          </el-form-item>
          <el-form-item label="pending_favs">
            <span>{{ props.row.pending_favs }}</span>
          </el-form-item>
          <el-form-item label="pending_total">
            <span>{{ props.row.pending_total }}</span>
          </el-form-item>
          <el-form-item label="variablePaths">
            <span>{{ props.row.variable_paths }}</span>
          </el-form-item>
          <el-form-item label="stability">
            <span>{{ props.row.stability }}</span>
          </el-form-item>
          <el-form-item label="bitmapCvg">
            <span>{{ props.row.bitmap_cvg }}</span>
          </el-form-item>
          <el-form-item label="uniqueCrashes">
            <span>{{ props.row.unique_crashes }}</span>
          </el-form-item>
          <el-form-item label="uniqueHangs">
            <span>{{ props.row.unique_hangs }}</span>
          </el-form-item>
          <el-form-item label="lastPath">
            <span>{{ props.row.last_path }}</span>
          </el-form-item>
          <el-form-item label="lastCrash">
            <span>{{ props.row.last_crash }}</span>
          </el-form-item>
          <el-form-item label="lastHangs">
            <span>{{ props.row.last_hang }}</span>
          </el-form-item>
          <el-form-item label="mode">
            <span>{{ props.row.target_mode }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>

    <el-table-column label="测试软件" prop="programName"> </el-table-column>
    <el-table-column label="Fuzz工具" prop="tool"> </el-table-column>
    <el-table-column label="Crash总数" prop="total_crashes"> </el-table-column>

    <el-table-column prop="path_cvg" label="路径覆盖率"> </el-table-column>
    <el-table-column prop="bitmap_cvg" label="bitmap_cvg"> </el-table-column>
  </el-table>
</template>



<script>
import { usedSoft } from "@/api/index";
export default {
  inject: ['reload'],
  name: "dashboard",
  data() {
    return {
      tableData: [
        {
          programName: "Xpdf",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "AFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "CollAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "Tortoise",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "7z",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "7z",
          tool: "Tortoise",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
        {
          programName: "Xpdf",
          tool: "MemAFL",
          path_cvg: "89%",
          total_crashes: "10",
          start_time: "1619065067",
          last_update: "1619067364",
          cycles_done: "0",
          execs_done: "284158",
          execs_per_sec: "187.56",
          paths_total: "2702",
          paths_favored: "621",
          paths_found: "736",
          paths_imported: "1949",
          max_depth: "2",
          cur_path: "77",
          pending_favs: "621",
          pending_total: "2701",
          variable_paths: "33",
          stability: "99.87%",
          bitmap_cvg: "19.25%",
          unique_crashes: "6",
          unique_hangs: "0",
          last_path: "1619067128",
          last_crash: "1619066593",
          last_hang: "0",
          target_mode: "default",
        },
      ],
      name: localStorage.getItem("ms_username"),
      time: this.getLocalTime(),
      avail_cpu: 60,
      notavail_cpu: 40,
      data: [
        {
          name: "2018/09/10",
          value: 1065,
        },
      ],
      //       tableData: [
      //     {
      //         id: '1',
      //         name: "sam2p",
      //         version: "0.49.4",
      //         timeStamp: null
      //     },
      //     {
      //         id: '2',
      //         name: "nasm",
      //         version: "2.10.07",
      //         timeStamp: null
      //     },
      //     {
      //         id: '3',
      //         name: "gzip",
      //         version: "1.10",
      //         timeStamp: null
      //     },
      //     {
      //         id: '4',
      //         name: "make",
      //         version: "4.3",
      //         timeStamp: null
      //     },
      //     {
      //         id: '5',
      //         name: "tack",
      //         version: "1.08",
      //         timeStamp: null
      //     },
      //     {
      //         id: '6',
      //         name: "patch",
      //         version: "2.7",
      //         timeStamp: null
      //     },
      //     {
      //         id: '7',
      //         name: "nano",
      //         version: "5.6",
      //         timeStamp: null
      //     }
      // ]
    };
  },

  computed: {
    role() {
      return this.name === "admin" ? "超级管理员" : "普通用户";
    },
  },
  watch:{
    '$route'(to,from){
      this.reload()
    }
  },
  methods: {
    tableRowClassName({ rowIndex }) {
      if (rowIndex === 1) {
        return "warning-row";
      } else if (rowIndex === 3) {
        return "success-row";
      }
      return "";
    },
    changeDate() {
      const now = new Date().getTime();
      this.data.forEach((item, index) => {
        const date = new Date(now - (6 - index) * 86400000);
        item.name = `${date.getFullYear()}/${
          date.getMonth() + 1
        }/${date.getDate()}`;
      });
    },
    sourceCode() {
      this.$router.push("/sourceCode");
    },
    sourceProgram() {
      this.$router.push("/sourceProgram");
    },
    history() {
      this.$router.push("/history");
    },
    getLocalTime() {
      var d = new Date();
      var aaa = d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate();
      return aaa;
    },
    getUsedSoft() {
      usedSoft().then((res) => {
        console.log(res.data);
        return res.data;
      });
    },
  },
};
</script>

<style scoped>
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}

@import url("//unpkg.com/element-plus/lib/theme-chalk/index.css");
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}

.el-row {
  margin-bottom: 20px;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
  color: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
  color: rgb(242, 94, 67);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

.mgb20 {
  margin-bottom: 10px;
  padding:0px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}

.schart {
  width: 100%;
  height: 300px;
}
</style>
