
<template>
  <el-form
    ref="this.form"
    :model="form"
    label-width="auto"
    :label-position="right"
    :rules="rules"
  >
    <el-form-item label="软件名称" prop="programName">
      <el-input v-model="form.programName" placeholder="请输入内容"></el-input>
    </el-form-item>

    <el-form-item label="上传源代码" prop="fileList">
      <el-upload
        class="sourceCode"
        drag
        action="/api/upload/uploadCode/"
        :before-remove="beforeRemove"
        multiple
        :file-list="form.fileList"
        :before-upload="onBeforeUploadCode"
        :on-success="codeRes"
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
    </el-form-item>

    <el-form-item label="fuzz软件" prop="name">
      <el-select v-model="form.name" placeholder="请选择使用的fuzz软件">
        <el-option label="afl" value="afl"></el-option>
        <el-option label="tortoise" value="tortoise"></el-option>
        <el-option label="mem" value="mem"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item label="编译命令" prop="compileCommand">
      <!-- <el-input
        type="compileCommand"
        :autosize="{ minRows: 2, maxRows: 4 }"
        placeholder="请输入内容"
        v-model="form.compileCommand"
      >
      </el-input> -->
      <el-select
        v-model="form.compileCommand"
        placeholder="请选择使用的编译命令"
      >
        <el-option label="llvm" value="llvm"></el-option>
        <el-option label="cmake" value="cmake"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item label="种子选取" size="small">
      <div>
        <el-radio-group v-model="form.seed">
          <el-radio-button
            v-for="city in cities"
            :label="city"
            :key="city"
            >{{ city }}</el-radio-button
          >
        </el-radio-group>
      </div>
    </el-form-item>

    <el-form-item label="上传输入文件">
      <div style="border 0px;">
        <el-upload
          class="inputFile"
          drag
          action="/api/upload/uploadInputFile/"
          :before-remove="beforeRemove"
          multiple
          :file-list="form.inputFile"
          :before-upload="onBeforeUploadInputFile"
          :on-success="inputFileRes"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        </el-upload>
      </div>
    </el-form-item>
    <!--         :on-success="getCodePath"            :on-success="getInputFilePath" -->
    <el-form-item label="时间选择">
      <el-input-number
        v-model="form.time"
        :step="1"
        :min="1"
        :max="24"
      ></el-input-number>
      小时
    </el-form-item>

    <el-form-item label="输入命令">
      <el-input
        type="inputCommand"
        :autosize="{ minRows: 2, maxRows: 4 }"
        placeholder="请输入内容"
        v-model="form.inputCommand"
      >
      </el-input>
    </el-form-item>

    <el-form-item label="参数">
      <el-input
        type="parameter"
        :autosize="{ minRows: 2, maxRows: 4 }"
        placeholder="请输入内容"
        v-model="form.parameter"
      >
      </el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { formdataTest } from "@/api/index";
import { defineComponent, ref } from "vue";
const cityOptions = ["602", "abw", "aes", "asm", "asn1", "bmi", "bmp", "bson", "bzip2", "certificate", "crl", "csv", "dercrl", "dif", "docx", "dxf", "ec", "elliptic", "eps", "flag", "flatbuffers", "flate", "fmt", "fodt", "freetype", "gif", "goast", "gob", "gofmt", "gopacket", "gorillamux", "gzip", "html", "http2", "httpreq", "httpresp", "jpeg", "json", "jsonrpc", "lzw", "mail", "mime", "mml", "mtp", "multipart", "nss", "ole", "parser", "path", "pct", "pcx", "pem", "pkcs", "pkix", "png", "ppm", "ppt", "protobuf", "qxp", "ras", "regexp", "rtf", "scrtf", "slk", "smtp", "snappy", "sqlparser", "stdhtml", "strings", "suffixrray", "svm", "tar", "tga", "tif", "tiff", "time", "tls", "tlsclient", "trace", "truetype", "url", "webdav", "webp", "websocketclient", "websocketserver", "wks", "wmf", "ww2", "ww6", "ww8", "xbm", "xls", "xlsx", "xml", "xpm", "zip", "zlib", "zmf"];
export default {
  data() {
    return {
      cities: cityOptions,
      fireList: [],
      form: {
        programName: ref(""),
        fileList: [],
        seed: [],
        name: "",
        inputFile: [],
        compileCommand: "",
        inputCommand: "",
        parameter: "",
        time: 1,
      },
      rules: {
        programName: [
          { required: true, message: "请输入软件名称", trigger: "blur" },
        ],
        fileList: [{ required: true, message: "请上传文件", trigger: "blur" }],
        name: [{ required: true, message: "请选择活动名称", trigger: "blur" }],
        compileCommand: [
          { required: true, message: "请选择编译命令", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    onSubmit() {
      this.$refs["this.form"].validate((valid) => {
        if (valid) {
          //  var formData = new FormData()
          let params = {
            fileList: this.form.fileList,
            seed: this.form.seed,
            name: this.form.name,
            inputFile: this.form.inputFile,
            compileCommand: this.form.compileCommand,
            inputCommand: this.form.inputCommand,
            parameter: this.form.parameter,
            time: this.form.time,
            programName: this.form.programName,
          };
          // formData.append('seed', this.form.seed),
          // formData.append('name',this.form.name),
          // formData.append('compileCommand', this.form.compileCommand),
          // formData.append('inputCommand', this.form.inputCommand),
          // formData.append('paramete', this.form.parameter),
          // formData.append('time',this.form.time),
          // console.log(formData),
          // axios({
          //   url: "http://127.0.0.1:8000/upload/sourceCode/",
          //   method: "post",
          //   data: Qs.stringify(params)
          // });
          console.log(params);
          formdataTest(params).then((res) => {
            console.log(res);
            if (res.data.status == 200) {
              alert("success!");
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    beforeRemove(file) {
      return this.$confirm(`确定移除 ${file.name}？`);
    },
    onBeforeUploadCode(file, fileList) {
      // formData = new FormData();
      // if (formData.length == 0) {
      // }
      // formData.append("myfile", file.file);
    },
    onBeforeUploadInputFile(file, fileList) {
      // formData = new FormData();
      // formData.append("inputFile", file.file);
    },
    codeRes(response, file, fileList) {
      console.log(response);
      this.form.fileList = response.file_path[0];
    },
    inputFileRes(response, file, fileList) {
      console.log(response);
      this.form.inputFile = response.inputFile[0];
    },
  },
};
</script>

<style>
</style>
