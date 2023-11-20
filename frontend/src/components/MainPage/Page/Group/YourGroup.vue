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
                  <div class="card-title-info">
                    <span>{{ card.title }}</span>
                    <span class="creator-info">创建人：{{ card.creator }}</span> <!-- 创建人信息 -->
                  </div>
                 <div class="button-container">
                    <div>
                      <span v-if="isManager" style="color: blue;">管理员</span>
                      <span v-else>普通成员</span>
                    </div>
                    <router-link to="Details">
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

const isManager = ref(true)

// Simulated card data
const cards = ref([
  { id: 1, title: 'group 1', image: './src/images/group-default-picture.png', creator: 'Alice' }, // 创建人信息
  { id: 2, title: 'group 2', image: './src/images/group-default-picture.png', creator: 'Bob' }, // 创建人信息
  { id: 3, title: 'group 3', image: './src/images/group-default-picture.png', creator: 'Charlie' }, // 创建人信息
  { id: 4, title: 'group 4', image: './src/images/group-default-picture.png', creator: 'David' } // 创建人信息
]);

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

.card-title-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.creator-info {
  color: #888; /* 创建人信息的颜色 */
  font-size: 14px; /* 创建人信息的字体大小 */
}
</style>
