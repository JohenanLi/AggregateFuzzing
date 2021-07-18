<template>
<div style="margin-top: 15px">
  <el-input
    placeholder="请输入搜索内容"
    v-model="input3"
    class="input-with-select"
  >
    <template #append>
      <el-button icon="el-icon-search"></el-button>
    </template>
  </el-input>

  <!-- <el-radio-group v-model="tabPosition" style="margin-bottom: 30px;">
    <el-radio-button label="top">top</el-radio-button>
    <el-radio-button label="right">right</el-radio-button>
    <el-radio-button label="bottom">bottom</el-radio-button>
    <el-radio-button label="left">left</el-radio-button>
  </el-radio-group> -->

  <el-tabs :tab-position="tabPosition" style="height: 200px;">
    <el-tab-pane label="用户管理">用户管理</el-tab-pane>
    <el-tab-pane label="配置管理">配置管理</el-tab-pane>
    <el-tab-pane label="角色管理">角色管理</el-tab-pane>
    <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
  </el-tabs>


</div>


</template>

<script>
  import { defineComponent, ref } from 'vue'
  export default {
    data() {
      return {
        tabPosition: 'left'
      };
    }
  };

// export default defineComponent ({
  
// })
</script>
