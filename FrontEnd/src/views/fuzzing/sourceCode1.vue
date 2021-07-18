<template>
    <div>
    <el-tabs :tab-position="tabPosition" style="height: 200px;">
    <el-tab-pane label="软件名称">
      <el-input class="input" v-model="form.programName" placeholder="请输入软件名称" clearable></el-input>
    </el-tab-pane>
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


