<template>
  <el-card :body-style="{ padding: '0px' }" class="custom-card">
    <!-- Card content -->
    <div class="image-container">
      <img :src="props.card.image" class="image" />
    </div>

    <div style="padding: 14px">
      <div class="card-title-info">
        <span>{{ props.card.title }}</span>
        <span class="creator-info">创建人：{{ props.card.creator }}</span>
      </div>
      <div class="button-container">
        <router-link to="Details">
          <el-button text class="button">查看详情</el-button>
        </router-link>
        <span>0/50</span>
        <el-button v-if="props.status === 0" @click="open" class="button">
          申请加入
        </el-button>
        <el-button v-else-if="props.status === 1" text class="button" disabled>
          审核中
        </el-button>
        <el-button v-else text type="danger" class="button" disabled>
          已加入
        </el-button>
      </div>
    </div>
  </el-card>
</template>


<script lang="ts" setup>
import { ref} from 'vue';
import { ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'


interface CardProps {
  card: {
    id: number;
    title: string;
    image: string;
    creator: string;
  };
  status: number;
}

const props  = defineProps<CardProps>();

const open = () => {
  ElMessageBox.alert('成功提交申请，正在审核', {
    confirmButtonText: 'OK',
    callback: (action: Action) => {},
  });
};

</script>

<style scoped>
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
  color: #070707; /* 按钮文本颜色 */
  background-color: #ffffff; /* 按钮背景色 */
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
