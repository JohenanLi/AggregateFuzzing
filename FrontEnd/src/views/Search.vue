<template>
  <!-- 搜索框 -->
  <div class="search_input">
    <el-input
      placeholder="请输入搜索内容"
      v-model="searchContent"
      class="input"
    ></el-input>

    <!-- 搜索按钮 -->
    <el-button v-on:click="searchFunction" plain icon="el-icon-search"
      >搜索</el-button
    >
  </div>
  <div class="table">
    <el-table :data="searchList" border style="width: 100% height: 100%" >
      <el-table-column prop="time" label="日期" width="250">
      </el-table-column>
      <el-table-column prop="programName" label="测试软件" width="250">
      </el-table-column>
      <el-table-column prop="fuzzer" label="Fuzz工具" width="250">
      </el-table-column>
      <el-table-column prop="crashes" label="漏洞总数" width="250">
      </el-table-column>
      <el-table-column prop="codeCoverage" label="平均路径覆盖率" width="250">
      </el-table-column>
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button @click.prevent="gotoprocess(scope.row)" type="text" size="large"
            >查看进度</el-button
          >
          <el-button @click="handleClick(scope.row)" type="text" size="large"
            >下载详细结果</el-button
          >
          <el-button
            @click.prevent="deleteRow(scope.$index, resultList)"
            type="text"
            size="large"
            >删除记录</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
// import { defineComponent, ref } from "vue";
import { searchGet } from "../api";
import 'element-plus/lib/theme-chalk/index.css';

export default {
  inject: ["reload"],
  name: "search",
   data() {
    return {
      searchList: [],
      searchContent: "",
    };
  },
  methods: {
     gotoprocess(row) {
      console.log(row.id);
       this.$router.push({
        name:'wait',
        params: {
          id: row.id
        }
    })
    },
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    searchFunction() {
      var searchContent = this.searchContent;
      if (searchContent) {
        let params = {
          content: searchContent,
        };
        searchGet(params).then((res) => {
          if (res.status == 200) {
            this.searchList = res.data;
          } else {
            console.log("error search!!");
            alert("搜索失败！");
            return false;
          }
        });
      } else if (searchContent.length == 0) {
        console.log("error search!!");
        alert("请输入搜索内容！");
      }
    },
  },
  watch: {
    $route(to, from) {
      this.reload();
    },
  },
};

</script>

<style scoped>
div {
  margin-top: 1%;
  align-items: center;
}
.input {
  width: 94%;
}
.search_input {
  margin: 1%;
}
.table {
  margin: 1%;
}
</style>