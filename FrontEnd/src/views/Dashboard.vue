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
                登录日期<br />
                {{ time }}
              </span>
              <el-divider direction="vertical"></el-divider>
              <span class="details"
                >登录地点<br />
                China</span
              >
              <el-divider direction="vertical"></el-divider>
              <span class="details"
                >检测次数<br />
                5</span
              >
            </el-space>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>

  <div class="table">
    <el-table :data="resultList" border style="width: 100% height: 100%">
      <el-table-column prop="time" label="日期" width="250">
        <!-- <span>{{ resultList.time }}</span> -->
      </el-table-column>
      <el-table-column prop="programName" label="测试软件" width="250">
        <!-- <span>{{ result.programName }}</span> -->
      </el-table-column>
      <el-table-column prop="fuzzer" label="Fuzz工具" width="250">
        <!-- <span>{{ result.fuzzer }}</span> -->
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞总数" width="250">
        <!-- <span>{{ result.crashes }}</span> -->
      </el-table-column>
      <el-table-column prop="codeCoverage" label="平均路径覆盖率" width="250">
        <!-- <span>{{ result.codeCoverage }}</span> -->
      </el-table-column>
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button
            @click.prevent="gotoprocess(scope.row)"
            type="text"
            size="large"
            >查看进度</el-button
          >
          <el-button @click="handleClick(scope.row)" type="text" size="large"
            >下载详细结果</el-button
          >
          <el-button
            @click.prevent="deleteRow(scope.$index, resultList)"
            type="text"
            size="large"
            >删除记录</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>

  <!-- <el-table :data="tableData" style="width: 100%">
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
        </el-form> -->
  <!-- </template>
    </el-table-column> -->

  <!-- <el-table-column label="测试软件" prop="programName"> </el-table-column>
    <el-table-column label="Fuzz工具" prop="tool"> </el-table-column>
    <el-table-column label="Crash总数" prop="total_crashes"> </el-table-column>

    <el-table-column prop="path_cvg" label="路径覆盖率"> </el-table-column>
    <el-table-column prop="bitmap_cvg" label="bitmap_cvg"> </el-table-column>
  </el-table> -->
</template>



<script>
import { usedSoft, resultGet } from "@/api/index";
import axios from "axios";
import QS from 'qs';

export default {
  inject: ["reload"],
  name: "dashboard",
  data() {
    return {
      // tableData: [],
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
      id: "",
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
  mounted() {
    this.getResult();
    this.timer = setInterval(() => {
      this.getResult();
      // console.log(this.$route.params.sum_ms);
    }, 30000);
  },
  methods: {
    handleClick(row) {
      alert("文件正在打包，请稍后");
      const data = {
        "id":row.id
      }
      axios({
        url:"api/download/",
        method: "POST",
        responseType: "arraybuffer",
        data: QS.stringify(data),
      })
        .then((res) => {
          const content = res.data;
          const blob = new Blob([content], { type: "application/zip" });
          const fileName = row.programName + "_" + row.fuzzer + ".zip";
          if ("download" in document.createElement("a")) {
            // 非IE下载
            const elink = document.createElement("a");
            elink.download = fileName;
            elink.style.display = "none";
            elink.href = window.URL.createObjectURL(blob);
            document.body.appendChild(elink);
            elink.click();
            window.URL.revokeObjectURL(elink.href); // 释放URL 对象
            document.body.removeChild(elink);
          } else {
            // IE10+下载
            navigator.msSaveBlob(blob, fileName);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    gotoprocess(row) {
      console.log(row.id);
      this.$router.push({
        name: "wait",
        params: {
          "programName":row.programName
        },
      });
    },
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
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
      resultGet().then((res) => {
        // console.log(res.data);
        this.resultList = res.data;
        console.log("this.resultList",this.resultList);
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
