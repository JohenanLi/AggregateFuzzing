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
    <p class="title">MemAFL</p>

    <!-- 单核信息 -->
    <el-table
      v-if="complete"
      :data="tableData"
      border
      style="width: 100%"
    >
      <el-table-column prop="core" label="CPU" width="110">
        <span>{{ result.mem.core }}</span>
      </el-table-column>
      <el-table-column prop="cycle" label="种子变异轮次" width="110">
        <span>{{ result.mem.cycle }}</span>
      </el-table-column>
      <el-table-column prop="speed" label="执行速度" width="110">
        <span>{{ result.mem.speed }}</span>
      </el-table-column>
      <el-table-column prop="path" label="当前路径" width="110">
        <span>{{ result.mem.path }}</span>
      </el-table-column>
      <el-table-column prop="pendig" label="等待路径" width="110">
        <span>{{ result.mem.pending }}</span>
      </el-table-column>
      <el-table-column prop="coverage" label="覆盖率" width="110"> 
        <span>{{ result.mem.coverage }}</span>
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞数量" width="110"> 
        <span>{{ result.mem.crashes }}</span>
      </el-table-column>
    </el-table>
    </el-card>
  <!-- 汇总信息 -->
  <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <el-table
      v-if="complete"
      :data="tableData"
      border
      style="width: 100%"
    >
      <el-table-column prop="CPU_all" label="CPU总数" width="110">
        <span>{{ result.mem.CPU_all }}</span>
      </el-table-column>
      <el-table-column prop="run_time" label="总运行时间" width="110">
        <span>{{ result.mem.run_time }}</span>
      </el-table-column>
      <el-table-column prop="run_time" label="总执行次数" width="110">
        <span>{{ result.mem.run_time }}</span>
      </el-table-column>
      <el-table-column prop="speed_sum" label="累计速度" width="110">
        <span>{{ result.mem.speed_sum }}</span>
      </el-table-column>
      <el-table-column prop="pendig_sum" label="总等待路径" width="110">
        <span>{{ result.mem.pending_sum }}</span>
      </el-table-column>
      <el-table-column prop="pendig_sum" label="平均等待路径" width="110">
        <span>{{ result.mem.pending }}</span>
      </el-table-column>
      <el-table-column prop="crashes_sum" label="总漏洞数量" width="110"> 
        <span>{{ result.mem.crashes_sum }}</span>
      </el-table-column>
    </el-table>
    </el-card>

    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <p class="title">Tortoise</p>
    <el-table
      v-if="complete"
      :data="tableData"
      border
      style="width: 100%"
    >
      <el-table-column prop="core" label="CPU" width="110">
        <span>{{ result.tortoise.core }}</span>
      </el-table-column>
      <el-table-column prop="cycle" label="种子变异轮次" width="110">
        <span>{{ result.tortoise.cycle }}</span>
      </el-table-column>
      <el-table-column prop="speed" label="执行速度" width="110">
        <span>{{ result.tortoise.speed }}</span>
      </el-table-column>
      <el-table-column prop="path" label="当前路径" width="110">
        <span>{{ result.tortoise.path }}</span>
      </el-table-column>
      <el-table-column prop="pendig" label="等待路径" width="110">
        <span>{{ result.tortoise.pending }}</span>
      </el-table-column>
      <el-table-column prop="coverage" label="覆盖率" width="110"> 
        <span>{{ result.tortoise.coverage }}</span>
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞数量" width="110"> 
        <span>{{ result.tortoise.crashes }}</span>
      </el-table-column>
    </el-table>
    </el-card>

     <!-- 汇总信息 -->
    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <el-table
      v-if="complete"
      :data="tableData"
      border
      style="width: 100%"
    >
      <el-table-column prop="CPU_all" label="CPU总数" width="110">
        <span>{{ result.tortoise.CPU_all }}</span>
      </el-table-column>
      <el-table-column prop="run_time" label="总运行时间" width="110">
        <span>{{ result.tortoise.run_time }}</span>
      </el-table-column>
      <el-table-column prop="run_time" label="总执行次数" width="110">
        <span>{{ result.tortoise.run_time }}</span>
      </el-table-column>
      <el-table-column prop="speed_sum" label="累计速度" width="110">
        <span>{{ result.tortoise.speed_sum }}</span>
      </el-table-column>
      <el-table-column prop="pendig_sum" label="总等待路径" width="110">
        <span>{{ result.tortoise.pending_sum }}</span>
      </el-table-column>
      <el-table-column prop="pendig_sum" label="平均等待路径" width="110">
        <span>{{ result.tortoise.pending }}</span>
      </el-table-column>
      <el-table-column prop="crashes_sum" label="总漏洞数量" width="110"> 
        <span>{{ result.tortoise.crashes_sum }}</span>
      </el-table-column>
    </el-table>
    </el-card>

    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <p class="title">AFLplusplus</p>
    <el-table
      v-if="complete"
      :data="tableData"
      border
      style="width: 100%"
    >
      <el-table-column prop="core" label="CPU" width="110">
        <span>{{ result.AFLpp.core }}</span>
      </el-table-column>
      <el-table-column prop="cycle" label="种子变异轮次" width="110">
        <span>{{ result.AFLpp.cycle }}</span>
      </el-table-column>
      <el-table-column prop="speed" label="执行速度" width="110">
        <span>{{ result.AFLpp.speed }}</span>
      </el-table-column>
      <el-table-column prop="path" label="当前路径" width="110">
        <span>{{ result.AFLpp.path }}</span>
      </el-table-column>
      <el-table-column prop="pendig" label="等待路径" width="110">
        <span>{{ result.AFLpp.pending }}</span>
      </el-table-column>
      <el-table-column prop="coverage" label="覆盖率" width="110"> 
        <span>{{ result.AFLpp.coverage }}</span>
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞数量" width="110"> 
        <span>{{ result.AFLpp.crashes }}</span>
      </el-table-column>
    </el-table>
    </el-card>
     <!-- 汇总信息 -->
    <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
    <el-table
      v-if="complete"
      :data="tableData"
      border
      style="width: 100%"
    >
      <el-table-column prop="CPU_all" label="CPU总数" width="110">
        <span>{{ result.AFLpp.CPU_all }}</span>
      </el-table-column>
      <el-table-column prop="run_time" label="总运行时间" width="110">
        <span>{{ result.AFLpp.run_time }}</span>
      </el-table-column>
      <el-table-column prop="run_time" label="总执行次数" width="110">
        <span>{{ result.AFLpp.run_time }}</span>
      </el-table-column>
      <el-table-column prop="speed_sum" label="累计速度" width="110">
        <span>{{ result.AFLpp.speed_sum }}</span>
      </el-table-column>
      <el-table-column prop="pendig_sum" label="总等待路径" width="110">
        <span>{{ result.AFLpp.pending_sum }}</span>
      </el-table-column>
      <el-table-column prop="pendig_sum" label="平均等待路径" width="110">
        <span>{{ result.AFLpp.pending }}</span>
      </el-table-column>
      <el-table-column prop="crashes_sum" label="总漏洞数量" width="110"> 
        <span>{{ result.AFLpp.crashes_sum }}</span>
      </el-table-column>
    </el-table>
    </el-card>
    </el-space>
    </div>
    <!-- 
    <div class="card">
      <el-space wrap :size="10">
          <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
            <h class="h">线程详细信息</h>
            <p class="result_individual" v-html="result.result_individual"></p>
          </el-card>
       

          <el-card shadow="hover" style="width: 100% height: 100%" :body-style="{ padding: '1%' }">
            <h class="h">线程汇总信息</h>
            <p class="result_summary" v-html="result.result_summary"></p>
          </el-card>
      
      </el-space>

    </div> -->
  </div>
</template>

<script>
import { processGet } from "../../api";
// import Header from '../../components/Header.vue';
export default {
  // components: { Header },
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
      timer: "",
      result: "",
      tableData: [],
    };
  },
  created() {},
  mounted() {
    this.DataView();
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
    this.timeOk = this.$route.params.timeLimit;

    // this.DataView();
    this.timer = setInterval(() => {
      this.DataView();
      console.log(this.$route.params.sum_ms);
    }, 5000);

    this.timer1 = setTimeout(this.close, this.$route.params.sum_ms);
  },
  methods: {
    close() {
      this.complete = false;
      clearTimeout(this.timer);
    },
    DataView() {
      let params;
      if(this.$route.params.id){
       params ={
          id: this.$route.params.id
        };
      }
      else{
        params = {
        fuzzer: this.$route.params.fuzzer,
        programName: this.$route.params.programName,
      };
      }
      processGet(params).then((res) => {
        if (res.status == 200) {
          this.result = res.data;
        }
      });
    },
  },
  watch: {
    $route(to, from) {
      this.reload();
    },
    result() {
      this.DataView();
    },
  },
  unmounted() {
    clearTimeout(this.timer);
    clearTimeout(this.timer1);
  },
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


