<template>
  <div class="main">
    <div class="box">
      <div v-if="complete" class="clip" :style="clipStyle"></div>
      <el-progress
        v-else
        type="circle"
        :percentage="100"
        :stroke-width="10"
        width="200"
        status="success"
      ></el-progress>
    </div>
    <div v-if="complete" class="tip">
      提交成功，请在{{ timeOk }}时查看最终结果。
    </div>
    <div v-else class="tip">已完成，请在个人主页查看结果</div>

    <div v-if="complete" class="card">
    <el-space wrap :size="8.5">
    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <p class="title" >MemAFL</p>

    <!-- 单核信息 -->
    <el-table
      v-if="complete"
      :data="result_MEMAFL"
      border
      style="width: 650"
      width="650"
      height="200"
    >
      <el-table-column prop="core" label="CPU" width="110" >
      </el-table-column>
      <el-table-column prop="cycle" label="种子变异轮次(次)" width="110">
      </el-table-column>
      <el-table-column prop="speed" label="执行速度(次每秒)" width="110">
      </el-table-column>
      <el-table-column prop="path" label="当前路径" width="110">
      </el-table-column>
      <el-table-column prop="pending" label="等待路径" width="110">
      </el-table-column>
      <el-table-column prop="coverage" label="覆盖率" width="110"> 
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞数量(个)" width="110"> 
      </el-table-column>
    </el-table>
    </el-card>
  <!-- 汇总信息 -->
  <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <p class="title" >MemAFL汇总</p>
    <el-table
      v-if="complete"
      :data="result_MEMAFL_sum"
      border
      height="200"
      width="650"
      style="width: 650"
    >
      <el-table-column prop="CPU_all" label="CPU总数(个)" width="110">
      </el-table-column>
      <el-table-column prop="run_time" label="总运行时间" width="110">
      </el-table-column>
      <el-table-column prop="total_execs" label="总执行次数(百万次)" width="110">
      </el-table-column>
      <el-table-column prop="speed_sum" label="累计速度(次每秒)" width="110">
      </el-table-column>
      <el-table-column prop="pending_sum" label="总等待路径(条)" width="110">
      </el-table-column>
      <el-table-column prop="pending" label="平均等待路径(条)" width="110">
      </el-table-column>
      <el-table-column prop="crashes_sum" label="独立漏洞数量(个)" width="110"> 
      </el-table-column>
    </el-table>
    </el-card>

    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <p class="title">Tortoise</p>
    <el-table
      v-if="complete"
      :data="result_TORTOISE"
      border
      height="200"
      style="width: 700"
    >
      <el-table-column prop="core" label="CPU" width="110">
      </el-table-column>
      <el-table-column prop="cycle" label="种子变异轮次(次)" width="110">
      </el-table-column>
      <el-table-column prop="speed" label="执行速度(次每秒)" width="110">
      </el-table-column>
      <el-table-column prop="path" label="当前路径" width="110">
      </el-table-column>
      <el-table-column prop="pending" label="等待路径" width="110">
      </el-table-column>
      <el-table-column prop="coverage" label="覆盖率" width="110"> 
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞数量(个)" width="110"> 
      </el-table-column>
    </el-table>
    </el-card>

     <!-- 汇总信息 -->
    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
      <p class="title" >Tortoise汇总</p>
    <el-table
      v-if="complete"
      :data="result_TORTOISE_sum"
      border
      height="200"
      style="width: 700"
    >
      <el-table-column prop="CPU_all" label="CPU总数(个)" width="110">
      </el-table-column>
      <el-table-column prop="run_time" label="总运行时间" width="110">
      </el-table-column>
      <el-table-column prop="total_execs" label="总执行次数(百万次)" width="110">
      </el-table-column>
      <el-table-column prop="speed_sum" label="累计速度(次每秒)" width="110">
      </el-table-column>
      <el-table-column prop="pending_sum" label="总等待路径(条)" width="110">
      </el-table-column>
      <el-table-column prop="pending" label="平均等待路径(条)" width="110">
      </el-table-column>
      <el-table-column prop="crashes_sum" label="独立漏洞数量(个)" width="110"> 
      </el-table-column>
    </el-table>
    </el-card>

    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <p class="title">DRILLER</p>
    <el-table
      v-if="complete"
      :data="result_AFL"
      border
      height="200"
      width="700"
      style="width: 700"
    >
      <el-table-column prop="core" label="CPU" width="110">
      </el-table-column>
      <el-table-column prop="cycle" label="种子变异轮次(次)" width="110">
      </el-table-column>
      <el-table-column prop="speed" label="执行速度(次每秒)" width="110">
      </el-table-column>
      <el-table-column prop="path" label="当前路径" width="110">
      </el-table-column>
      <el-table-column prop="pending" label="等待路径" width="110">
      </el-table-column>
      <el-table-column prop="coverage" label="覆盖率" width="110"> 
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞数量(个)" width="110"> 
      </el-table-column>
    </el-table>
    </el-card>
     <!-- 汇总信息 -->
    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
      <p class="title" >AFLpp汇总</p>
    <el-table
      v-if="complete"
      :data="result_AFL_sum"
      border
      height="200"
      style="width: 700"
    >
      <el-table-column prop="CPU_all" label="CPU总数(个)" width="110">
      </el-table-column>
      <el-table-column prop="run_time" label="总运行时间" width="110">
      </el-table-column>
      <el-table-column prop="total_execs" label="总执行次数(百万次）" width="110">
      </el-table-column>
      <el-table-column prop="speed_sum" label="累计速度(次每秒)" width="110">
      </el-table-column>
      <el-table-column prop="pending_sum" label="总等待路径(条)" width="110">
      </el-table-column>
      <el-table-column prop="pending_sum" label="平均等待路径(条)" width="110">
      </el-table-column>
      <el-table-column prop="crashes_sum" label="独立漏洞数量(个)" width="110"> 
      </el-table-column>
    </el-table>
    </el-card>
    </el-space>
    </div>
  </div>
</template>

<script>
import { processGet } from "../../api";
export default {
  inject: ["reload"],
  name: "wait",
  data() {
    return {
      //进度条
      clipStyle: {
        transform: "rotate(" + 3.6 * 0 + "deg)",
      },
      //基本参数
      complete: true,
      timeOk: "",
      result_MEMAFL: [],
      result_MEMAFL_sum: [],
      result_TORTOISE: [],
      result_TORTOISE_sum: [],
      result_AFL: [],
      result_AFL_sum: [],
      tableData: [],
      sum_ms: ""
    };
  },
  created(){
  },

  mounted() {
    //进度条
    let rotate = 0;
    setInterval(() => {
      if (rotate >= 100) {
        rotate = 0;
      }
      rotate++;

      let transform = "rotate(" + 3.6 * rotate + "deg)";

      this.$data.clipStyle.transform = transform;
    }, 20);

    //从后端获取数据
  
    this.DataView();
    this.timer = setInterval(() => {
      this.DataView();
    }, 5000);

    // this.timer1 = setTimeout(this.close, this.sum_ms);
    // this.startCount();
    
  },
  methods: {
    close() {
      this.complete = false;
      clearTimeout(this.timer1);
       clearInterval(this.timer);
    },
    startCount () {
      // this.closeCount();
      this.timer = setInterval(() => {
      this.DataView();
    }, 5000);
    
    },
    closeCount () {
    if (this.timer) {
     clearInterval(this.timer)
   }
    },
    DataView() {
      let params={
        programName: this.$route.params.programName,
      };
      processGet(params).then((res) => {       
        this.sum_ms = res.data.sum_ms;
        this.timeOk = res.data.timeOk;
        this.result_MEMAFL = res.data.MEMAFL;
        this.result_MEMAFL_sum = res.data.MEMAFL_sum;
        this.result_TORTOISE = res.data.TORTOISE;
        this.result_TORTOISE_sum = res.data.TORTOISE_sum;
        this.result_AFL = res.data.DRILLER;
        this.result_AFL_sum = res.data.DRILLER_sum;
        // if (res.status == 200) {
        //   this.result = res.data;
        //  this.sum_ms = res.data.sum_ms;
        // }
        if(res.status == 500){
          this.complete = false;
          this.close();
        }

      });
    },
  },
  watch: {
    $route(to, from) {
      this.reload();
    },
    // result() {
    //   this.DataView();
    // },
  },
  unmounted() {
    clearInterval(this.timer);
    clearTimeout(this.timer1);
  },
  beforeUnmount(){
    clearInterval(this.timer);
    clearTimeout(this.timer1);
  }
};
</script>

<style scoped>
.title {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 200%;
  font-weight: bold;
  color: rgb(78, 156, 233);
}
.box {
  margin: 2% 0% 0% 2%;
  /* position: relative; */
  width: 200px;
  height: 200px;
  /* overflow: hidden; */
}
.card {
  margin: 2% 2% 0% 2%;
  align-items: center;
}
.clip {
  height: 100%;
  box-sizing: border-box;
  border-top: 20px solid #5cb87a;
  border-left: 20px solid #5cb87a;
  border-right: 20px solid #ccc;
  border-bottom: 20px solid #ccc;
  border-radius: 50%;
}
.tip {
  /* margin: 1%; */
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 200%;
  font-weight: bold;
  color: #5cb87a;
  align-content: center;
}
</style>


