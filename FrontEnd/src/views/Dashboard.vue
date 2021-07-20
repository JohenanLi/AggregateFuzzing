<template>
  <div>
    <el-row :gutter="18">
      <el-col :span="24">
        <el-card shadow="hover" class="mgb20" style="height: 252px">
          <div class="user-info">
            <img src="../assets/img/img.jpg" class="user-avator" alt />
            <div class="user-info-cont">
              <div class="user-info-name">{{ name }}</div>
              <div>{{ role }}</div>
            </div>
          </div>
          <div class="time_place">
            <el-space wrap :size="large">
            <span class="details">
              登录日期<br>
            {{time}}
            </span>
            <el-divider direction="vertical"></el-divider>
            <span class="details">登录地点<br>
            China</span>
            <el-divider direction="vertical"></el-divider>
            <span class="details">检测次数<br>
            5</span>
            </el-space>
            <!-- <div class="user-info-list">
            上次登录时间：
            <span>{{ time }}</span>
          </div>
          <div class="user-info-list">
            上次登录地点：
            <span>长沙</span> -->
            <!-- </div> -->
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>

  <el-table :data="tableData" style="width: 100%">
    <el-table-column type="expand">
      <template #default="">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="programName">
            <span>{{ resultList.programName }}</span>
          </el-form-item>
          <el-form-item label="tool">
            <span>{{ resultList.tool }}</span>
          </el-form-item>
          <el-form-item label="pathCoverage">
            <span>{{ resultList.path_cvg }}</span>
          </el-form-item>
          <el-form-item label="totalCrashes">
            <span>{{ resultList.total_crashes }}</span>
          </el-form-item>
          <el-form-item label="startTime">
            <span>{{ resultList.start_time }}</span>
          </el-form-item>
          <el-form-item label="lastUpdate">
            <span>{{ resultList.last_update }}</span>
          </el-form-item>
          <el-form-item label="queueCycles">
            <span>{{ resultList.cycles_done }}</span>
          </el-form-item>
          <el-form-item label="execveCalls">
            <span>{{ resultList.execs_done }}</span>
          </el-form-item>
          <el-form-item label="execs_per_sec">
            <span>{{ resultList.execs_per_sec }}</span>
          </el-form-item>
          <el-form-item label="totalPaths">
            <span>{{ resultList.paths_total }}</span>
          </el-form-item>
          <el-form-item label="favoredPaths">
            <span>{{ resultList.paths_favored }}</span>
          </el-form-item>
          <el-form-item label="pathsFound">
            <span>{{ resultList.paths_found }}</span>
          </el-form-item>
          <el-form-item label="importedPaths">
            <span>{{ resultList.paths_imported }}</span>
          </el-form-item>
          <el-form-item label="max_depth">
            <span>{{ resultList.max_depth }}</span>
          </el-form-item>
          <el-form-item label="currentPaths">
            <span>{{ resultList.cur_path }}</span>
          </el-form-item>
          <el-form-item label="pending_favs">
            <span>{{ resultList.pending_favs }}</span>
          </el-form-item>
          <el-form-item label="pending_total">
            <span>{{ resultList.pending_total }}</span>
          </el-form-item>
          <el-form-item label="variablePaths">
            <span>{{ resultList.variable_paths }}</span>
          </el-form-item>
          <el-form-item label="stability">
            <span>{{ resultList.stability }}</span>
          </el-form-item>
          <el-form-item label="bitmapCvg">
            <span>{{ resultList.bitmap_cvg }}</span>
          </el-form-item>
          <el-form-item label="uniqueCrashes">
            <span>{{ resultList.unique_crashes }}</span>
          </el-form-item>
          <el-form-item label="uniqueHangs">
            <span>{{ resultList.unique_hangs }}</span>
          </el-form-item>
          <el-form-item label="lastPath">
            <span>{{ resultList.last_path }}</span>
          </el-form-item>
          <el-form-item label="lastCrash">
            <span>{{ resultList.last_crash }}</span>
          </el-form-item>
          <el-form-item label="lastHangs">
            <span>{{ resultList.last_hang }}</span>
          </el-form-item>
          <el-form-item label="mode">
            <span>{{ resultList.target_mode }}</span>
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
import { usedSoft, resultGet } from "@/api/index";
import axios from "axios";

export default {
  inject: ["reload"],
  name: "dashboard",
  data() {
    return {
      tableData: [],
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
      resultList: [],
      id: 1,
    };
  },

  computed: {
    role() {
      return this.name === "admin" ? "超级管理员" : "普通用户";
    },
  },
  watch: {
    $route(to, from) {
      this.reload();
    },
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
    getResult() {
      let params = {
        id: this.id,
      };
      resultGet(params).then((res) => {
        this.resultList = res.data;
      });
    },
  },
};
</script>

<style scoped>
.details {
  text-align: center;
  float: left;
}
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
  margin-bottom: 0px;
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
.time_place {
  margin: 1% 0% 0% 36%;
}
.user-info {
  display: flex;
  align-items: center;
  margin: 0% 0% 0% 40%;
  /* padding-bottom: 20px; */
  /* border-bottom: 2px solid #ccc; */
  /* margin-bottom: 20px; */
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
  margin-bottom: 0px;
  padding: 0px;
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
