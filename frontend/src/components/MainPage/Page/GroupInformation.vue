<template>
    <el-button @click="add">create group</el-button>
    <el-scrollbar max-height="400px">
      <el-row>
        <el-col v-for="card in cards" :key="card.id" :span="8" >
          <el-card :body-style="{ padding: '0px' }" class="custom-card">
            <!-- Card content -->
            <img :src="card.image" class="image" />
            <div style="padding: 14px">
              <span>{{ card.title }}</span>
              <div class="bottom">
                <el-button text class="button">查看详情</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-scrollbar>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue';

  // Simulated card data
  const cards = ref([
    { id: 1, title: 'group 1', image: './src/images/group-default-picture.png' },
    { id: 2, title: 'group 2', image: './src/images/group-default-picture.png' },
  ]);
  
  const add = () => {
    cards.value.push({
        id: cards.value.length + 1,
        title: `group ${cards.value.length + 1}`,
        image: `./src/images/group-default-picture.png`,
    });
  };

  </script>
  
  <style scoped>.time {
    font-size: 12px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .button {
    padding: 0;
    min-height: auto;
  }
  
  .image {
    width: 400px;
    height: 200px;
    display: block;
  }
  </style>
  