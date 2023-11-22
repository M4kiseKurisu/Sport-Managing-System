<template>
      <el-scrollbar class="scrollbar" max-height="100%">
        <el-row v-for="(group, index) in groups" :key="index">
          <el-col v-for="card in group" :key="card.id" :span="8">
            <el-card :body-style="{ padding: '0px' }" class="custom-card">
               <!-- Card content -->
              <div class="image-container">
                <div v-if="card.pic !== null">
                  <img :src="'http://127.0.0.1:8000' + card.pic" class="image" />
                </div>
                <div v-else>
                  <img :src="defaultImage" class="image" />
                </div>
              </div>
              <div style="padding: 14px">
                  <div class="card-title-info">
                    <span>{{ card.group_name }}</span>
                    <span class="creator-info">创建人：{{ card.creator }}</span> <!-- 创建人信息 -->
                  </div>
                 <div class="button-container">
                    <div>
                      <span v-if="isManager" style="color: blue;">管理员</span>
                      <span v-else>普通成员</span>
                    </div>
                    <router-link :to="{ path: '/Page/GroupInformation/Details', 
                        query: { 
                            groupName: card.group_name, 
                            description: card.group_desc, 
                            image: card.pic
                        }
                    }">
                        <el-button text class="button">查看详情</el-button>
                    </router-link>

                    <span>{{ card.capacity }}/{{ card.maximum }}</span>
                    <el-button text @click="open(card)" class="button">退出</el-button>
                 </div>
               </div>
             </el-card>
           </el-col>
         </el-row>
       </el-scrollbar>
</template>

<script lang="ts">
import { ref } from 'vue';
import { ElMessageBox } from 'element-plus';
import type { Action } from 'element-plus';
import axios from 'axios'

export default {
  data() {
    return {
      groupList: [], // 从后端获取的所有团体数据 
      input: "",
      keyword: "",
      status: "",
      msg: ""
    }
  },
  created() {
      const storedUid = sessionStorage.getItem('uid');
      if (storedUid) {
        const uid = JSON.parse(storedUid);
        axios({
          method: "GET",
          url: "http://127.0.0.1:8000/api/group/view",
          params: {
            uid: uid
          }
        }).then((result) => {
          this.groupList = result.data.list;
          this.status = result.data.status;
          this.msg = result.data.msg;
        }).catch((error) => {
          console.error('Error fetching group data:', error);
        });
    } else {
        console.error('UID not found in sessionStorage');
    }
  },

  computed: {
    groups() {
      const joinedGroup: any[] = [];
      for (let i = 0; i < this.groupList.length; i++) {
        if (this.groupList[i].is_joined === true) {
          joinedGroup.push(this.groupList[i]);
        }
      }
      const groups: any[][] = [];
      for(let i = 0; i < joinedGroup.length; i+=3){
          groups.push(joinedGroup.slice(i, i+3))
      }
      return groups;
    }
  },

  setup() {
    const isManager = ref(true);
    const defaultImage = "./src/images/group-default-picture.png"
    // const open = (cardToDelete: any) => {
    //   ElMessageBox.alert('退出成功', {
    //     confirmButtonText: 'OK',
    //     callback: (action: Action) => {
    //       if (action === 'confirm') {
    //         deleteCard(cardToDelete);
    //       }
    //     },
    //   });
    // };

    // const deleteCard = (cardToDelete: any) => {
    //   // 找到要删除的卡片在数组中的索引
    //   const index = cards.value.findIndex((card) => card.id === cardToDelete.id);

    //   if (index !== -1) {
    //     // 如果找到了匹配的卡片索引，就从 cards 数组中删除该卡片
    //     cards.value.splice(index, 1);
    //   }
    // };

    return {
      isManager,
      open,
      defaultImage
      // deleteCard,
    };
  },
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
