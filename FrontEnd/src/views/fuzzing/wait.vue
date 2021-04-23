
<template>
<div style="center">
<el-progress type="circle" :percentage="nowProgress" v-if="progress_type=='normal'" :width="circle_width"></el-progress>
<el-progress type="circle" :percentage="100" status="success" v-if="progress_type=='success'" :width="circle_width"></el-progress>
<el-progress type="circle" :percentage="70" status="warning" v-if="progress_type=='warning'" :width="circle_width"></el-progress>
<el-progress type="circle" :percentage="50" status="exception" v-if="progress_type=='exception'" :width="circle_width"></el-progress>
</div>
</template>
<script>
export default {
  name:"wait",
  data(){
    return{
      circle_width:500,
      progress_type: "normal",
      nowProgress:0
    }
  },
  created(){
    this.timer = setInterval(this.updateProgress, 100);
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
    }
  }
}
</script>


