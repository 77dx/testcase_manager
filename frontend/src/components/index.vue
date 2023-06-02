<template>
  <div class="container">
      <el-container>
        <el-header>Header</el-header>
        <el-container>
          <el-aside width="200px">Aside</el-aside>
          <el-main>Main</el-main>
        </el-container>
      </el-container>
  </div>
</template>

<style>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #FFFFFF;
    color: #333;
    text-align: left;

  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .container{
    position: absolute;
    top:0;
    left: 0;
    width: 100%;
    height:100%;
  }
  .el-submenu [class^=el-icon-]{
    height: 20px;
  }
</style>
