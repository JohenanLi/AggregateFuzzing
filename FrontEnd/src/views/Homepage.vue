<template>
 
  <!-- <div class="loginbottom" id="login" align="right">
    <el-link :underline="false" class="login" >注 册</el-link>

    <el-link :underline="false" class="sign" >登 录</el-link>
  </div> -->

  <div class="centerBottom" align="center">

  <div class="logobottom" id="logo">
    <p class="title"><i class="el-icon-search"></i>FuzzTotal</p>
  </div>

  
  <div class="explainbottom" align="left">
    <p class="explain">欢迎使用FuzzTotal,您可以选择上传源代码或者可执行文件进行漏洞挖掘，也可以搜索本系统所拥有资源。</p>
    </div>

  <div class="Function_button" align="center">
    <el-row>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img
            src="../assets/img/上传源文件.jpg"
            class="image"
              height="200"
            width="200"
          />
          <div style="padding: 1%">
            
            <div class="bottom">
              <!-- <time class="time">{{ currentDate }}</time> -->
              <el-button v-on:click="gotoSourceCode" type="primary" plain class="button"><i class="el-icon-upload el-icon--right"></i>源代码文件上传</el-button>
            </div>
          </div>

        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img src="../assets/img/上传可执行文件.jpg" class="image" height="200"
            width="200"/>
          <div style="padding: 1%">
            <div class="bottom" >
              <el-button type="primary" v-on:click="gotoSourceProgram" plain class="button"><i class="el-icon-upload el-icon--right"></i>可执行文件上传</el-button>
            </div>
          </div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img src="../assets/img/find.jpg" class="image" height="200"
            width="200"/>

          <div style="padding: 1% ">
            <div class="bottom">
              <el-button type="primary" v-on:click="gotoSearch" plain class="button" icon="el-icon-search">请输入搜索内容</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>

  </div>
</template>
<script>
//import { defineComponent } from '@vue/composition-api'

export default {
  inject: ['reload'],
  name: "logo",
  data() {
    return {};
  },
  methods: {
    gotoSourceCode(){
      this.$router.push('/sourceCode');
    },
    gotoSourceProgram(){
      this.$router.push('/sourceProgram');
    },
    gotoSearch(){
      this.$router.push('/Search');
    }
  },
  watch:{
    '$route'(to,from){
      this.reload()
    }
  },
  computed: {},
};
</script>
<style scoped>
div {
  margin-top: 5%;
  margin-left: 3.5%;
}
.Function_button {
  margin-top: 5%;
  margin-left: 4%;
}
.centerbottom{
  margin: 0%；
}
.title {
  margin-top: 5%;
  margin-left: 0%;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size:400%;
  font-weight: bold;
  color: rgb(78, 156, 233);
}
.explain {
  margin-top: 5%;
  margin-left: 4%;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size:x-large;

  color: rgb(128, 129, 129);
}
.time {
  font-size: 13px;
  color: #999;
}
.explainbottom {
  width: 1000px;
  height: 20px;
  margin: 20px 20px 20px 0px;
  
}
.logobottom {
  height:70px;
}
.bottom {
  /* margin-top: 13px; */
  margin-bottom: 2%;
  margin-left: 25%;
  line-height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 20px;
  min-height: auto;
  margin-right: 50%;
}
.sign {
  color:rgb(78, 156, 233);
  font-size:large;
  padding: 0px 7px;
}
.login {
  color: rgb(248, 251, 255);
  font-size:large;
  box-sizing: border-box;
  border-radius: 10px;
  padding: 0px 7px;
  background: rgb(123, 177, 231);
}
.loginbottom {
  margin: 0 0 0 0;
}
.image {
  width: 70%;
  display: block;
  text-align: center;
  margin-left:15%;
  margin-top: 10%;
}
.el-card {
  text-align: center;
}
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 500px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 900px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style> 