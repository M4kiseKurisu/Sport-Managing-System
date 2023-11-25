<template>
  <el-card :body-style="{ padding: '0px' }" class="custom-card">
    <!-- Card content -->
    <div class="image-container">
      <div v-if="props.card.pic !== null">
        <img :src="'http://127.0.0.1:8000' + props.card.pic" class="image" />
      </div>
      <div v-else>
        <img :src="defaultImage" class="image" />
      </div>
    </div>

    <div style="padding: 14px">
      <div class="card-title-info">
        <span>{{ props.card.group_name }}</span>
        <span class="creator-info">创建人：{{ props.card.creator }}</span>
      </div>
      <div class="button-container">
        <router-link :to="{ path: '/Page/GroupInformation/Details', 
            query: { 
                groupName: card.group_name, 
                description: card.group_desc, 
                image: card.pic,
                father: 'GroupList'
            }
        }">
            <el-button text class="button">查看详情</el-button>
        </router-link>
        <span>{{ props.card.capacity }}/{{ props.card.maximum }}</span>
        <el-button v-if="props.card.is_joined === false" @click="applicate(card.gid)" class="button">
          申请加入
        </el-button>
        <el-button v-else text type="danger" class="button" disabled>
          已加入
        </el-button>
      </div>
    </div>
  </el-card>
</template>


<script lang="ts" setup>
import { ElMessage, ElMessageBox } from 'element-plus'
import axios from 'axios'

const defaultImage = "./src/images/group-default-picture.png"

interface CardProps {
  card: {
    gid: number;
    group_name: string;
    pic: string;
    creator: string;
    is_joined: boolean;
    maximum: number;
    capacity: number;
    group_desc: ""
  };
  status: number;
  msg:string;
  
}

const props  = defineProps<CardProps>();

const applicate = (gid) => {
  ElMessageBox.prompt('发送你的申请', {
    confirmButtonText: '提交申请',
    cancelButtonText: '取消申请',
    inputPattern: /.*/,
    inputErrorMessage: '请填写申请',
  }).then(({ value }) => {
      if (!value) {
        ElMessage({
          type: 'warning',
          message: '申请信息不能为空',
        });
        return;
      }

      console.log(gid)
      // 发送申请
      axios.post('http://127.0.0.1:8000/api/group/join', {
        uid: sessionStorage.getItem('uid'),
        gid: gid,
        content: value,
      }).then(response => {
          const { status, msg } = response.data;

          if (status === true) {
            ElMessage({
              type: 'success',
              message: msg,
            });
          } else {
            ElMessage({
              type: 'error',
              message: msg,
            });
          }
        }).catch(error => {
          console.error('发送申请时出错:', error);
          ElMessage({
            type: 'error',
            message: '申请发送失败，请稍后重试',
          });
        });
    }).catch(() => {
      ElMessage({
        type: 'info',
        message: '你已取消申请',
      });
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
