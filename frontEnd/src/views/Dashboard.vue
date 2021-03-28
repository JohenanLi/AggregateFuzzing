<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card shadow="hover" class="mgb20" style="height: 252px">
          <div class="user-info">
            <img src="../assets/img/img.jpg" class="user-avator" alt />
            <div class="user-info-cont">
              <div class="user-info-name">{{ name }}</div>
              <div>{{ role }}</div>
            </div>
          </div>
          <div class="user-info-list">
            上次登录时间：
            <span>2021-03-28</span>
          </div>
          <div class="user-info-list">
            上次登录地点：
            <span>长沙</span>
          </div>
        </el-card>

        <el-card shadow="hover">
          <template #header>
            <div class="clearfix">
              <span>语言详情</span>
            </div>
          </template>
          Vue
          <el-progress :percentage="71.3" color="#42b983"></el-progress
          >JavaScript
          <el-progress :percentage="24.1" color="#f1e05a"></el-progress>CSS
          <el-progress :percentage="13.7"></el-progress>HTML
          <el-progress :percentage="5.9" color="#f56c6c"></el-progress>
        </el-card>
      </el-col>

      <el-col :span="16">
        <el-row :gutter="25" type="flex" class="row-bg" justify="space-between">
          <el-col :span="16" style="height: 180px">
            <el-card shadow="hover">
              <div class="grid-content grid-con-1">
                <i class="el-icon-document grid-con-icon"></i>
                <div class="grid-cont-right">
                  <el-button type="text" @click="sourceCode()"
                    ><div class="grid-num">上传源代码并编译</div></el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="16" style="height: 180px">
            <el-card shadow="hover">
              <div class="grid-content grid-con-2">
                <i class="el-icon-box grid-con-icon"></i>
                <div class="grid-cont-right">
                  <el-button type="text" @click="sourceProgram()"
                    ><div class="grid-num">上传源程序代码</div></el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="16" style="height: 180px">
            <el-card shadow="hover">
              <div class="grid-content grid-con-3">
                <i class="el-icon-loading grid-con-icon"></i>
                <div class="grid-cont-right">
                  <el-button type="text" @click="history()"
                    ><div class="grid-num">历史记录</div></el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "dashboard",
  data() {
    return {
      name: localStorage.getItem("ms_username"),
      todoList: [
        {
          title: "今天要修复100个bug",
          status: false,
        },
        {
          title: "今天要修复100个bug",
          status: true,
        },
      ],
      data: [
        {
          name: "2018/09/10",
          value: 1065,
        },
      ],
    };
  },
  computed: {
    role() {
      return this.name === "admin" ? "超级管理员" : "普通用户";
    },
  },

  methods: {
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
  },
};
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
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

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
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
  margin-bottom: 20px;
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
