<template>
  <div id="logo" align="center">
    <p class="title"><i class="el-icon-search"></i>FuzzTotal</p>
  </div>
  <div></div>

  <div>
    <el-row>
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }">
          <img
            src="../assets/img/上传源文件.jpg"
            class="image"
            height="200"
            width="300"
          />
          <div style="padding: 14px">
            
            <div class="bottom">
              <time class="time">{{ currentDate }}</time>
              <el-button type="primary" plain class="button"><i class="el-icon-upload el-icon--right"></i>源代码文件上传</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }">
          <img src="../assets/img/上传可执行文件.jpg" class="image" height="200"
            width="300"/>
          <div style="padding: 14px">
            <div class="bottom">
              <el-button type="primary" plain class="button"><i class="el-icon-upload el-icon--right"></i>可执行文件上传</el-button>
            </div>
          </div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card :body-style="{ padding: '0px' }">
          <img src="../assets/img/find.jpg" class="image" height="200"
            width="300"/>
          <div style="padding: 14px">
            <div class="bottom">
              <el-button type="primary" plain class="button" icon="el-icon-search">请输入搜索内容</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script>
//import { defineComponent } from '@vue/composition-api'

export default {
  name: "logo",
  data() {
    return {};
  },
  methods: {},
  computed: {},
};
</script>
<style scoped>
div {
  margin-top: 60px;
  margin-left: 50px;
}
.title {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: xxx-large;
  color: rgb(78, 156, 233);
}
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 20px;
  min-height: auto;
  margin-right: 50%;
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