<template>
<div style="margin-top: 1% ">
  <el-input
    placeholder="请输入搜索内容"
    v-model="searchContent"
    type="text"
    class="input-with-select"
  >
    <template #append>
      <el-button @click="searchFunction" icon="el-icon-search"></el-button>
    </template>
  </el-input>

</div>


</template>

<script>
  import { defineComponent, ref } from 'vue'
  export default {
    data() {
      return {
       
      };
    }
  };

</script>

<style scoped>
.input-with-select {

}
</style>