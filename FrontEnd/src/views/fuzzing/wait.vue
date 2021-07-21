<template>
  <!-- <div> -->
  <div class="box">
    <div class="clip" :style="clipStyle"></div>
    <span class="tip">提交成功，请在{{ timeOk }}时查看最终结果。</span>
  </div>
  <!-- <div>
    {{ master }}
  </div> -->
  <!-- </div> -->
</template>

<script>
import { processGet } from '../../api';
export default {
  inject: ['reload'],
  name:"wait",
  data(){
    return{
      //进度条
      clipStyle: {
        transform: "rotate(" + 3.6 * 0 + "deg)",
      },
      //基本参数
      master: "jfsdaklfjlasdjfljsadfkljl",

      // timeOk: this.$route.params.fileTime
      timeOk:"",
      fileName:"",
      timeLimit:"",
    }
  },
  created(){
    console.log(this.fileName,this.timeLimit);
    // this.DataView()
  },
  mounted(){
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
    this.fileName=localStorage.getItem("fileName");
    this.timeLimit = localStorage.getItem(this.fileName);
    this.timeOk = this.timeLimit;
    console.log(this.fileName,this.timeLimit);
  },

  methods:{
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
  margin:1%;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 200%;
  font-weight: bold;
  color: #5cb87a;
}
</style>


