<template>
  <el-card :body-style="{ padding: '0px' }" class="custom-card">
    <!-- Card content -->
    <div class="image-container">
        <img :src="card.image" class="image" />
    </div>

    <div style="padding: 14px">
      <span>{{ card.title }}</span>
      <div class="button-container">
        <div v-if="isManager" class="icon-container">
      <el-icon><UserFilled /></el-icon>
      </div>
        <router-link to="/GroupMainPage">
          <el-button text class="button">查看详情</el-button>
        </router-link>
        <span>0/50</span>
        <el-button text @click="open" class="button">申请加入</el-button>
      </div>
    </div>
  </el-card>
</template>


<script lang="ts" setup>
import {
     UserFilled
   } from '@element-plus/icons-vue'
import { ref} from 'vue';
import { defineProps } from 'vue';
import { ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'

const props = defineProps({
    group: Object, // Group data as prop
});

const isManager = ref(true)

interface card {
id: Number;
title: string;
image: string; // 新增字段
}

const card = ref<card>({
  id: 1,
  title: 'Group',
  image: './src/images/group-default-picture.png'
});

// 更新卡片信息的函数
const updateCard = (newCard: card) => {
  card.value = newCard;
};

const open = () => {
  ElMessageBox.alert('成功提交申请，正在审核', {
    // if you want to disable its autofocus
    // autofocus: false,
    confirmButtonText: 'OK',
    callback: (action: Action) => {

    },
  })
}
</script>

<style scoped>
/* 调整 el-scrollbar 大小 */
.scrollbar {
width: 100%; /* 设置宽度 */
height: 400px; /* 设置高度 */
}

/* 调整 el-card 大小 */
.custom-card {
height: 175px;
width: 90% /* 设置卡片高度 */
}

.button-container {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
  color: #fff; /* 按钮文本颜色 */
  background-color: #409eff; /* 按钮背景色 */
}

.image-container {
  /* Set container size */
  width: 100%;
  height: 100px; /* Set container height */

  /* Set container as flex to center image */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* Hide overflow */
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

.icon-container {
  align-self: flex-start; /* Adjust alignment as needed */
  margin: 5px; /* Adjust margin as needed */
  z-index: 1;
}

.icon {
  font-size: 20px; /* Adjust icon size as needed */
  /* Add any additional styles for your icon */
}
</style>
