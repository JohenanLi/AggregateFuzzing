
<template>
  <div class="bottom">
    <el-form
      ref="this.form"
      :model="form"
      label-width="80px"
      label-position="top"
      :rules="rules"
    >
      <el-tabs :tab-position="tabPosition" style="height: 100%">
        <el-tab-pane label="参数输入"
          >参数输入
          <div class="parmInput">
            <el-form-item label="软件名称" prop="programName">
              <el-input
                class="input"
                v-model="form.programName"
                placeholder="请输入软件名称"
                clearable
              ></el-input>
            </el-form-item>

            <el-tooltip placement="bottom" effect="light">
              <template #content >
                请输入需要进行模糊测试的<br/>
                二进制文件的相对路径！
              </template>

            </el-tooltip>

            <el-tooltip placement="bottom" effect="light">
              <template #content >
              请输入运行时所需参数！
              </template>

            <el-form-item label="输入命令">
              <el-input
                class="input"
                type="inputCommand"
                :autosize="{ minRows: 2, maxRows: 4 }"
                placeholder="请输入内容"
                v-model="form.inputCommand"
              >
              </el-input>
            </el-form-item>
            </el-tooltip>

            <el-tooltip placement="bottom" effect="light">
              <template #content >
              请输入模糊测试时间！
              </template>
        
              <el-form-item label="时间选择">
              <el-input-number
                v-model="form.hour"
                :step="1"
                :min="0"
                :max="24"
              ></el-input-number>
              小时
            

              <el-input-number
                v-model="form.minute"
                :step="5"
                :min="0"
                :max="60"
              ></el-input-number>
              分钟
            </el-form-item>


              </el-tooltip>

             
            

          </div>
        </el-tab-pane>

        <el-tab-pane label="文件上传"
          >文件上传
          <div class="parmInput">
            <el-tooltip placement="bottom" effect="light">
              <template #content >
              请上传需要进行模糊测试的二进制文件压缩包！
              </template>
            <el-form-item label="上传文件" prop="fileList">
              <el-upload
                class="sourceCode"
                drag
                action="http://fuzz.wolongdanxin.top/api/upload/uploadCode/"
                :before-remove="beforeRemove"
                multiple
                :file-list="form.fileList"
                :before-upload="onBeforeUploadCode"
                :on-success="codeRes"
              >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">
                  将压缩文件拖到此处，或<em>点击上传</em>
                </div>
              </el-upload>
            </el-form-item>
            </el-tooltip>

          </div>
        </el-tab-pane>

        <el-tab-pane label="种子文件"
          >种子文件
          <div class="parmInput">
            <el-tooltip placement="bottom" effect="light">
              <template #content >
              请上传种子文件！
              </template>
            <el-form-item label="上传种子文件">
              <div> 
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
                  <div class="el-upload__text">
                    将输入文件拖到此处，或<em>点击上传</em>
                  </div>
                </el-upload>
              </div>
            </el-form-item>
            </el-tooltip>

            <!-- 种子选取 -->
            <el-tooltip placement="bottom" effect="light">
              <template #content >
              请选取种子文件！
              </template>
            <el-form-item prop="seed" label="种子选取">
            <div class="block" >
              <el-cascader
                v-model="form.seed"
                placeholder="试试搜索：doct"
                :options="cityOptions"
                filterable
                clearable
              ></el-cascader>
            </div>
          </el-form-item>
          </el-tooltip>

          </div>
        </el-tab-pane>
        <!-- <el-tab-pane label="定时任务"
          >定时任务
         
        </el-tab-pane> -->
      </el-tabs>
    </el-form>

     <div class="submit">
    <el-form-item size="large">
      <el-button type="primary" @click="onSubmit">提交</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </div>

  </div>
</template>

<script>
import { formdataTest } from "@/api/index";
import { defineComponent, ref } from "vue";
import { ElMessage } from 'element-plus';
export default {
  inject: ["reload"],
  data() {
    return {
      tabPosition: "left",
      // cities: cityOptions,
      fireList: [],
      form: {
        programName: ref(""),
        fileList: [],
        seed: "",
        name: "MEMAFL",
        inputFile: [],
        compileCommand: "",
        inputCommand: "",
        prePara: "",
        postPara: "",
        hour: 0,
        minute: 5,
      },
      rules: {
        programName: [
          { required: true, message: "请输入软件名称", trigger: "blur" },
        ],
        fileList: [{ required: true, message: "请上传文件", trigger: "blur" }],
        // name: [{ required: true, message: "请选择fuzz软件名称", trigger: "blur" }],
        compileCommand: [
          { required: false, message: "请输入编译命令", trigger: "blur" },
        ],
        seed:[{
          required: true, message: "请选择种子文件", trigger: "blur"
        }]
      },
      cityOptions:[{
           value: 'simple',
          label: '常用种子',
          children: [{
            value: '文档文件',
            label: '文档文件',
            children: [{
              value: 'rtf',
              label: 'rtf'
            },
            {
              value: 'docx',
              label: 'docx'
            },
            {
              value: 'html',
              label: 'html'
            },
            {
              value: 'pdf',
              label: 'pdf'
            },
            {
              value: 'ppt',
              label: 'ppt'
            },
            {
              value: 'abw',
              label: 'abw'
            },
            {
              value: 'csv',
              label: 'csv'
            }]
          }, {
            value: '压缩文件',
            label: '压缩文件',
            children: [{
              value: 'zip',
              label: 'zip'
            },
            {
              value: 'gzip',
              label: 'gzip'
            },
            {
              value: '7z',
              label: '7z'
            },
            {
              value: 'bzip2',
              label: 'bzip2'
            },
            {
              value: 'lzw',
              label: 'lzw'
            }]
          },
          {
            value: '图像文件',
            label: '图像文件',
            children: [{
              value: 'bmp',
              label: 'bmp'
            },
            { 
              value: 'gif',
              label: 'gif'
            },
            { 
              value: 'jpeg',
              label: 'jpeg'
            },
            { 
              value: 'png',
              label: 'png'
            },
            { 
              value: 'tif',
              label: 'tif'
            },
            {
              value: 'dif',
              label: 'dif'
            },
            {
              value: 'dxf',
              label: 'dxf'
            },
            {
              value: 'eps',
              label: 'eps'
            }]
          },
          {
            value: '声音文件',
            label: '声音文件',
            children: [{
              
            }]
          },
          {
            value: '动画文件',
            label: '动画文件',
            children: [{
              
          }]
          },
          {
            value: '系统文件',
            label: '系统文件',
            children: [{
              
          }]
          },
          {
            value: '语言文件',
            label: '语言文件',
            children: [{
              value: 'asm',
              label: 'asm'
          },
          {
            value: 'asn1',
            label: 'asn1'
          },
          {
            value: 'bson',
            label: 'bson'
          },
          {
            value: 'ec',
            label: 'ec'
          },
          {
            value: 'gofmt',
            label: 'gofmt'
          },
          {
            value: 'gopacket',
            label: 'gopacket'
          },
          {
            value: 'gorillamux',
            label: 'gorillamux'
          },
          {
            value: 'json',
            label: 'json'
          },
          {
            value: 'jsonrpc',
            label: 'jsonrpc'
          }]
          }]
        }, {
          value: '不常用文件',
          label: '不常用文件',
          children: [{
              
            }]
        }],
      options: [
        {
          value: "AFL",
          label: "AFL",
        },
        {
          value: "TORTOISE",
          label: "TORTOISE",
        },
        {
          value: "MEMAFL",
          label: "MEMAFL",
        },
      ],
      valuetype: "MEMAFL",
    };
  },
  watch: {
    $route(to, from) {
      this.reload();
    },
  },
  methods: {
    
    onSubmit() {
      this.$refs["this.form"].validate((valid) => {
          //加载
        const myloading = this.$loading({
          lock: true,
          text: '参数正在提交，请稍候',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        });
        if (valid) {

          let params = {
            fileList: this.form.fileList,
            seed: this.form.seed[this.form.seed.length - 1],
            name: this.form.name,
            inputFile: this.form.inputFile,
            compileCommand: this.form.compileCommand,
            inputCommand: this.form.inputCommand,
            prePara: this.form.prePara,
            postPara: this.form.postPara,
            hour: this.form.hour,
            minute: this.form.minute,
            programName: this.form.programName,
          };
          formdataTest(params).then((res) => {
            console.log(res);
            if (res.status == 200) {
              alert("success!");
              myloading.close();
            this.gotowait(res.data.msg,res.data.sum_ms);
            }
            else {
            myloading.close();
            console.log("error submit!!");
            alert('提交失败！');
        }
          })
        .catch(function (error) {
          // if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            myloading.close();
            console.log("error submit!!");
            alert('提交失败！');
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
          // } else if (error.request) {
          //   // The request was made but no response was received
          //   // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          //   // http.ClientRequest in node.js
          //   console.log(error.request);
          // } else {
          //   // Something happened in setting up the request that triggered an Error
          //   console.log('Error', error.message);
          // }
          console.log(error.config);
        });
        } else {
          myloading.close();
          console.log("error submit!!");
          alert('提交失败！');
          return false;
        }
      });
    },
    gotowait(timeLimit,sum_ms){
      this.$router.push({
        name:'wait',
        params: {
                  fuzzer:this.form.name,
                  programName:this.form.programName,
                  timeLimit:timeLimit,
                  sum_ms: sum_ms
        }
    })
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
      this.form.fileList = response.file_path[0];
    },
    inputFileRes(response, file, fileList) {
      this.form.inputFile = response.inputFile[0];
    },
  },
};
</script>

<style lang="less" scoped>
/deep/.el-tabs {
  margin-top: 20px;
  padding: 20px 0 0 20px;
  font-size: 25px;
  font-weight: 600;
  .el-tabs__header {
    .el-tabs__nav-wrap {
      .el-tabs__nav-scroll {
        .el-tabs__nav {
          .el-tabs__item {
            font-size: 25px;
            font-weight: 400;
            height: 60px;
            // color: #808080;
          }
          .el-tabs__active-bar {
            height: 0;
          }
          .el-tabs__item.is-active {
            color: #409eff;
          }
        }
      }
    }
  }
}
/deep/.el-form-item__label {
  font-size: 20px;
}
.submit {
  margin: 0% 0px 0px 60%;
}
.tab {
  margin: 0px 0px 80px 0px;
}
.parmInput {
  margin: 0px 10px 10px 10%;
}
.bottom {
  margin: 0px 20% 5px 10%;
  height: 88%;
  width: 88%;
}
.input {
  width: 700px;
}
</style>
