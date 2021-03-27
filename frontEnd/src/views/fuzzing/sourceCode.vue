<template>
<div id="page-wrapper">
    <div id="page-inner">
        <div class="row">
            <div class="col-md-12"> 
                <h1 class="page-header" style="color: rgb(46, 100, 201);">
                    源代码上传 <small style="color: rgb(122, 172, 247);">uploading by source</small>
                </h1>
                <!-- Advanced Tables -->
                <div class="panel panel-info">
                    <div class="panel-body">
                        <div class="table-responsive">
                            <table class="table  table-bordered table-hover " id="dataTables-example">
                                <thead>
                                    <tr>
                                        <!--<th>id</th>-->
                                        <th>filePath</th>
                                        <th>name</th>
                                        <th>seed</th>
                                        <th>inputFile</th>
                                        <th>参数</th>
                                        <th>compileCommand</th>
                                        <th>inputCommand</th>
                                        <th>操作</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="odd gradeX">
                                        <form enctype="multipart/form-data" action="/upload/sourceCode/" method="post">
                                            <!--<td>{{obj.id}}</td>-->
                                            <td> <input type="file"  name="myfile"></td>
                                            <td class="il-con">
                                               
                                                <div>
                                                    <select   name="name" id="name">
                                                        <option value="afl">afl</option>
                                                        <option value="tortoise">tortoise</option>
                                                        <option value="emem">emem</option>
                                                    </select>
                                                </div>
                                            </td>
                                            <td>
                                                
                                                    <div class="dropdown">
                                                        <button type="button" class="btn btn-primary dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            style="background-color:unset; color: rgb(66, 65, 65);">
                                                            种子选择
                                                        </button>
                                                        <div class="dropdown-menu">
                                                            {% for seed in seedList %}
                                                            <option><input type="checkbox" name="seed"
                                                                    value={{seed}} />{{seed}}</option>
                                                            {% endfor %}
                                                        </div>
                                                    </div>
                                                
                                            </td>
                                            <td><input type="file" name="inputFile" /></td>
                                            <td class="center"><input type="text" name="parameter"
                                                    value='{{ obj.parameter}}'></td>
                                            <td><input type="text" name="compileCommand" value='{{obj.compileCommand}}'>
                                            </td>
                                            <td><input type="text" name="inputCommand" value='{{obj.inputCommand}}'>
                                            </td>
                                            <td><input type="submit" value="提交"></td>
                                        </form>
                                    </tr>
                                </tbody>
                            </table>
                            <form>
                                <br />
                            </form>
                        </div>
                    </div>
                    <div class="panel-footer">fuzzing</div>
                </div>
                <!--End Advanced Tables -->
            </div>
        </div>
    </div>
</template>
