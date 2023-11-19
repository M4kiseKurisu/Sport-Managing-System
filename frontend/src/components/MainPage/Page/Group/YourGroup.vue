<template>
       <el-scrollbar class="scrollbar" max-height="100%">
         <el-row>
           <el-col v-for="card in cards" :key="card.id" :span="8" >
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
                    <el-button text @click="open(card)" class="button">退出</el-button>
                 </div>
               </div>
             </el-card>
           </el-col>
         </el-row>
       </el-scrollbar>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'

const isManager = ref(false)

// Simulated card data
const cards = ref([
  { id: 1, title: 'group 1', image: './src/images/group-default-picture.png' },
  { id: 2, title: 'group 2', image: './src/images/group-default-picture.png' },
  { id: 3, title: 'group 3', image: './src/images/group-default-picture.png' },
  { id: 4, title: 'group 4', image: './src/images/group-default-picture.png' },
]);

interface Groups {
name: string;
avatar: string;
description: string; // 新增字段
}

const tableData: Groups[] = [
{
  name: 'group1',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group2',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group3',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group4',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group5',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group6',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group7',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
{
  name: 'group8',
  avatar: './src/images/emptyAvatar.png',
  description: '寻找志同道合的伙伴~'
},
]

const open = (cardToDelete: any) => {
  ElMessageBox.alert('退出成功', {
    confirmButtonText: 'OK',
    callback: (action: Action) => {
      if (action === 'confirm') {
        deleteCard(cardToDelete);
      }
    },
  });
};

const deleteCard = (cardToDelete: any) => {
  // 找到要删除的卡片在数组中的索引
  const index = cards.value.findIndex((card) => card.id === cardToDelete.id);

  if (index !== -1) {
    // 如果找到了匹配的卡片索引，就从 cards 数组中删除该卡片
    cards.value.splice(index, 1);
  }
};
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
}

</style>
