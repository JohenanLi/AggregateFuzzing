<template>
  <div>
  <div class="progress">
    <el-progress
      type="circle"
      :stroke-width="20"
      :color="progress_color"
      :percentage="nowProgress"
      :width="circle_width"
    ></el-progress>
    <span class="tip"
      >提交成功，请在{{ timeOk }}时查看最终结果。</span
    >
  </div>
  <div>
    {{ master }}
  </div>
  </div>
</template>

<script>
import { processGet } from '../../api';
export default {
  inject: ['reload'],
  name:"wait",
  data(){
    return{
      master: {},
      circle_width:200,
      nowProgress:20,
      progress_color:'#5cb87a',
      timeOk: this.$route.params.fileTime
    }
  },
  created(){
    this.timer = setInterval(this.updateProgress, localStorage.getItem(FileList));
    // this.DataView()
  },
  methods:{
    updateProgress(){
        this.$nextTick(() => {
      this.nowProgress += 1;
      if(this.nowProgress == 100)
      {
        clearInterval(this.timer);
        this.progress_type = "success";
      }

    });
    }, 
    DataView(){
    let params = {
        // fileName : this.$route.params.fileId
    };
      processGet(params).then((res) => {
            console.log(res);
            if (res.data.status == 200) {
              alert("success!");
            this.master = res.data.master
            }
          });
    },
    timer () {
      return setTimeout(() => {
        this.DataView()
      }, 1000)
    },
    
  },
    watch:{
    '$route'(to,from){
      this.reload()
    },
     fourData() {
      this.timer()
    }
    }
}
</script>

<style scoped>
.progress {
  margin: 0% 5%;
}
.tip {
  margin: 10%;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 200%;
  font-weight: bold;
  color: #5cb87a;
}
</style>


