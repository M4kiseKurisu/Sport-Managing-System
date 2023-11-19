<template>
<el-button text @click="addNewGroup">Create Group</el-button>
<el-row :gutter="20">
  <el-col :span="8">

      <!-- 单项活动展示 1-->
      <div class="group">
          <GroupCard />
      </div>

      <!-- 单项活动展示 4-->
      <div class="group">
          <GroupCard />
      </div>

      <!-- 单项活动展示 7-->
      <div class="group">
          <GroupCard />
      </div>

  </el-col>

  <el-col :span="8">

      <!-- 单项活动展示 2-->
      <div class="group">
          <GroupCard />
      </div>

      <!-- 单项活动展示 5-->
      <div class="group">
          <GroupCard />
      </div>

      <!-- 单项活动展示 8-->
      <div class="group">
          <GroupCard />
      </div>

  </el-col>

  <el-col :span="8">

      <!-- 单项活动展示 3-->
      <div class="group">
          <GroupCard />
      </div>
      
      <div class="group">
          <GroupCard />
      </div>

      <div class="group">
          <GroupCard />
      </div>

  </el-col>
</el-row>

<!-- 最下方需要实现换页功能，查看更多的活动，使用分页器元素 -->

<div class="pagination">
  <el-pagination background layout="prev, pager, next" :total="1000" @current-change="handlePageChange" />
</div>
</template>
<script lang="ts">
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'
import GroupCard from "../../Components/GroupCard.vue";

export default {
  data() {
    return {
      input: ""
    }
  },
  components: {
    GroupCard
  },
  methods: {
    handlePageChange(pageNo) {
      // 处理分页变化
    },
    addNewGroup() {
      ElMessageBox.alert('This is a message', 'Title', {
        confirmButtonText: 'OK',
        callback: (action: Action) => {
          ElMessage({
            type: 'info',
            message: `action: ${action}`,
          })
        },
      })
    }
  }
}
</script>
  
<style scoped>
.el-row {
    margin-top: 40px;
}

.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.header {
    display: flex;
    align-items: center;
}

.group {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

.pagination {
    display: flex;
    justify-content: flex-end;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-right: 30px;
}

.search {
    width: 200px;
    margin-left: 10px;
}

.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>