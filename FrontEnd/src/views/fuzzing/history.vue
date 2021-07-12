
<template>
    <el-table :data="tableData" style="width: 100%">
        <el-table-column type="expand">
            <template #default="props">
                <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="programName">
                        <span>{{ props.row.programName }}</span>
                    </el-form-item>
                    <el-form-item label="tool">
                        <span>{{ props.row.tool}}</span>
                    </el-form-item>
                    <el-form-item label="pathCoverage">
                        <span>{{ props.row.path_cvg}}</span>
                    </el-form-item>
                    <el-form-item label="totalCrashes">
                        <span>{{ props.row.total_crashes}}</span>
                    </el-form-item>
                    <el-form-item label="startTime">
                        <span>{{ props.row.start_time }}</span>
                    </el-form-item>
                    <el-form-item label="lastUpdate">
                        <span>{{ props.row.last_update }}</span>
                    </el-form-item>
                    <el-form-item label="queueCycles">
                        <span>{{ props.row.cycles_done }}</span>
                    </el-form-item>
                    <el-form-item label="execveCalls">
                        <span>{{ props.row.execs_done}}</span>
                    </el-form-item>
                    <el-form-item label="execs_per_sec">
                        <span>{{ props.row.execs_per_sec}}</span>
                    </el-form-item>
                    <el-form-item label="totalPaths">
                        <span>{{ props.row.paths_total}}</span>
                    </el-form-item>
                    <el-form-item label="favoredPaths">
                        <span>{{ props.row.paths_favored}}</span>
                    </el-form-item>
                    <el-form-item label="pathsFound">
                        <span>{{ props.row.paths_found}}</span>
                    </el-form-item>
                    <el-form-item label="importedPaths">
                        <span>{{ props.row.paths_imported}}</span>
                    </el-form-item>
                    <el-form-item label="max_depth">
                        <span>{{ props.row.max_depth}}</span>
                    </el-form-item>
                    <el-form-item label="currentPaths">
                        <span>{{ props.row.cur_path}}</span>
                    </el-form-item>
                    <el-form-item label="pending_favs">
                        <span>{{ props.row.pending_favs}}</span>
                    </el-form-item>
                    <el-form-item label="pending_total">
                        <span>{{ props.row.pending_total}}</span>
                    </el-form-item>
                    <el-form-item label="variablePaths">
                        <span>{{ props.row.variable_paths}}</span>
                    </el-form-item>
                    <el-form-item label="stability">
                        <span>{{ props.row.stability}}</span>
                    </el-form-item>
                    <el-form-item label="bitmapCvg">
                        <span>{{ props.row.bitmap_cvg}}</span>
                    </el-form-item>
                    <el-form-item label="uniqueCrashes">
                        <span>{{ props.row.unique_crashes}}</span>
                    </el-form-item>
                    <el-form-item label="uniqueHangs">
                        <span>{{ props.row.unique_hangs}}</span>
                    </el-form-item>
                    <el-form-item label="lastPath">
                        <span>{{ props.row.last_path}}</span>
                    </el-form-item>
                    <el-form-item label="lastCrash">
                        <span>{{ props.row.last_crash}}</span>
                    </el-form-item>
                    <el-form-item label="lastHangs">
                        <span>{{ props.row. last_hang}}</span>
                    </el-form-item>
                    <el-form-item label="mode">
                        <span>{{ props.row. target_mode}}</span>
                    </el-form-item>
                </el-form>
            </template>
        </el-table-column>


        <el-table-column label="测试软件" prop="programName">
        </el-table-column>
        <el-table-column label="Fuzz工具" prop="tool">
        </el-table-column>
        <el-table-column label="Crash总数" prop="total_crashes">
        </el-table-column>

        <el-table-column prop="path_cvg" label="路径覆盖率">
        </el-table-column>
        <el-table-column prop="bitmap_cvg" label="bitmap_cvg">
        </el-table-column>
    </el-table>
</template>

<script>
  export default {
    methods: {
      tableRowClassName({ rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 3) {
          return 'success-row';
        }
        return '';
      }
    },
    data() {
      return {
       tableData: [{
                programName: 'Xpdf',
                tool: 'AFL',
                path_cvg: '89%',
                total_crashes: '10',
                start_time: '1619065067',
                last_update: '1619067364',
                cycles_done: '0',
                execs_done: '284158',
                execs_per_sec: '187.56',
                paths_total: '2702',
                paths_favored: '621',
                paths_found: '736',
                paths_imported: '1949',
                max_depth: '2',
                cur_path: '77',
                pending_favs: '621',
                pending_total: '2701',
                variable_paths: '33',
                stability: '99.87%',
                bitmap_cvg: '19.25%',
                unique_crashes: '6',
                unique_hangs: '0',
                last_path: '1619067128',
                last_crash: '1619066593',
                last_hang: '0',
                target_mode: 'default',
            }]
      }
    }
  }
</script>

<style>
.el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

@import url("//unpkg.com/element-plus/lib/theme-chalk/index.css");
.demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }

</style>
