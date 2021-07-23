<template>
  <div class="main">
    <div class="box">
      <div v-if="complete" class="clip" :style="clipStyle"></div>
      <el-progress v-else type="circle" :percentage="100" :stroke-width="10" width="200" status="success"></el-progress>
    </div>
    <div v-if="complete" class="tip">提交成功，请在{{ timeOk }}时查看最终结果。</div>
    <div v-else class="tip">已完成，请在个人主页查看结果</div>
    <p class="result_individual" v-html="result.result_individual"></p>
    <p class="result_summary" v-html="result.result_summary"></p>
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
      timer:"",
      result:"",
    };
  },
  created() {
   
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
    this.timeOk = this.$route.params.timeLimit;

    // this.DataView();
    this.timer = setInterval(()=>{ 
      this.DataView();
      console.log(this.$route.params.sum_ms);
    }, 5000);
    
    this.timer1 = setTimeout(this.close,this.$route.params.sum_ms);
  },
  methods: {
    close() {
      this.complete=false;
    },
    DataView() {
      let params = {
        fuzzer: this.$route.params.fuzzer,
        programName: this.$route.params.programName,
      };
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
.box {
  margin: 2% 0% 0% 2%;
  /* position: relative; */
  width: 200px;
  height: 200px;
  /* overflow: hidden; */
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


