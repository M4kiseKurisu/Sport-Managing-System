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
                      <span style="color: blue;">{{ card.type }}</span>
                    </div>
                    <router-link :to="{ path: '/Page/GroupInformation/Details', 
                        query: { 
                            gid: card.gid,
                            groupName: card.group_name, 
                            description: card.group_desc, 
                            image: card.pic,
                            father: 'YourGroup',
                            type: card.type
                        }
                    }">
                        <el-button text class="button">查看详情</el-button>
                    </router-link>

                    <span>{{ card.capacity }}/{{ card.maximum }}</span>
                    <el-button text @click="quit(card)" class="button">退出</el-button>
                 </div>
               </div>
             </el-card>
           </el-col>
         </el-row>
       </el-scrollbar>
</template>

<script>
import { ElMessageBox, ElMessage } from 'element-plus';
import axios from 'axios';

export default {
  data() {
    return {
      groupList: [],
      input: "",
      keyword: "",
      status: "",
      msg: "",
    };
  },
  methods: {
    getData() {
      const storedUid = sessionStorage.getItem('uid');
      if (storedUid) {
        const uid = JSON.parse(storedUid);
        axios({
          method: "GET",
          url: "http://127.0.0.1:8000/api/user/group",
          params: { uid: uid }
        }).then((result) => {
          if( result.data.status ){
            this.groupList = result.data.list;
            this.status = result.data.status;
            this.msg = result.data.msg;
          }
        }).catch((error) => {
          console.error('Error fetching group data:', error);
        });
      } else {
        console.error('UID not found in sessionStorage');
      }
    },
    quit(card) {
      let msg = '是否确认退出';
      if (card.type == '创建人') {
        msg = '是否确认退出并解散团体';
      }
      ElMessageBox.confirm(msg,
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
        }
      ).then(() => {
        axios.post('http://127.0.0.1:8000/api/group/exit', {
          uid: sessionStorage.getItem('uid'),
          gid: card.gid
        }).then(response => {
          ElMessage({
            type: 'success',
            message: '退出成功',
          });
          this.getData();
        }).catch(error => {
          ElMessage({
            type: 'error',
            message: '退出失败，请重试',
          });
        });
      }).catch(() => {
        ElMessage({
          type: 'info',
          message: '你已取消操作',
        });
      });
    },
  },
  created() {
    this.getData();
  },
  computed: {
    groups() {
      const groups = [];
      for (let i = 0; i < this.groupList.length; i += 3) {
        groups.push(this.groupList.slice(i, i + 3));
      }
      return groups;
    },
  },
  setup() {
    const defaultImage = "./src/images/group-default-picture.png";
    return {
      defaultImage
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
  color: #888; /* 创建人人信息的颜色 */
  font-size: 14px; /* 创建人人信息的字体大小 */
}
</style>
