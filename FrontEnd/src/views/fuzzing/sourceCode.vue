
<template>
  <el-form ref="form" :model="form" label-width="auto" :label-position="right">
    <el-form-item label="上传源代码">
      <el-upload
        class="sourceCode"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        :before-remove="beforeRemove"
        multiple
        :file-list="form.fileList"
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
    </el-form-item>

    <el-form-item label="fuzz软件">
      <el-select v-model="form.name" placeholder="请选择使用的fuzz软件">
        <el-option label="afl" value="afl"></el-option>
        <el-option label="tortoise" value="tortoise"></el-option>
        <el-option label="emem" value="emem"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item label="种子选取" size="small">
      <div>
        <el-checkbox-group v-model="form.seed">
          <el-checkbox-button
            v-for="city in cities"
            :label="city"
            :key="city"
            >{{ city }}</el-checkbox-button
          >
        </el-checkbox-group>
      </div>
    </el-form-item>

<el-form-item label="上传输入文件">
  <div style="border 0px;">
<el-upload
  class="inputFile"
  drag
  action="https://jsonplaceholder.typicode.com/posts/"
  :before-remove="beforeRemove"
  :file-list="form.fileList"
  multiple>
  <i class="el-icon-upload"></i>
  <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
</el-upload>
</div>
</el-form-item>

<el-form-item label="时间选择">
  <el-input-number v-model="form.time" :step="5"></el-input-number> 分钟
</el-form-item>

<el-form-item label="编译命令">
<el-input
  type="compileCommand"
  :autosize="{ minRows: 2, maxRows: 4}"
  placeholder="请输入内容"
  v-model="form.compileCommand">
</el-input>
</el-form-item>

<el-form-item label="输入命令">
<el-input
  type="inputCommand"
  :autosize="{ minRows: 2, maxRows: 4}"
  placeholder="请输入内容"
  v-model="form.inputCommand">
</el-input>
</el-form-item>

<el-form-item label="参数">
<el-input
  type="parameter"
  :autosize="{ minRows: 2, maxRows: 4}"
  placeholder="请输入内容"
  v-model="form.parameter">
</el-input>
</el-form-item>



    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
const cityOptions = [
  "602",
  "abw",
  "bmi",
  "cdr",
  "cgm",
  "cmx",
  "dif",
  "docx",
  "dxf",
  "eot",
  "eps",
  "fh",
  "fodg",
  "fodp",
  "fods",
  "fodt",
  "html",
  "hwp",
  "key6",
  "lwp",
  "met",
  "mml",
  "mtp",
  "ole",
  "pcd",
  "pct",
  "pcx",
  "pmd",
  "ppm",
  "ppt",
  "pptx",
  "psd",
  "pub",
  "qpw",
  "qxp",
  "ras",
  "rtf",
  "scrtf",
  "sda",
  "sdc",
  "sdd",
  "sdw",
  "slk",
  "svm",
  "tga",
  "tif",
  "vdx",
  "vsd",
  "vsdx",
  "wks",
  "wmf",
  "ww2",
  "ww6",
  "ww8",
  "xbm",
  "xls",
  "xlsx",
  "xpm",
  "zip",
  "zmf",
];
export default {
  data() {
    return {
      cities: cityOptions,
      form: {
        fileList: [],
        seed: [],
        name: "",
        inputFile: [],
        compileCommand:"",
        inputCommand:"",
        parameter:"",
        time:5
      },
    };
  },
  methods: {
    onSubmit() {
      console.log("submit!");
    },
    beforeRemove(file) {
      return this.$confirm(`确定移除 ${file.name}？`);
    },
  },
};
</script>

<style>
</style>
