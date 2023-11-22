<template>
<div class="button-row">
  <el-button text @click="addNewGroup">Create Group</el-button>
  <div class="searchTitle">
    <div class="searchBox">
      <el-input v-model="keyword" placeholder="输入查询信息"></el-input>
    </div>
    <el-button @click="search">查 询</el-button>
  </div>
</div>

<div>
    <el-scrollbar class="scrollbar" max-height="100%">
      <el-row v-for="(page, index) in paginatedGroups" :key="index">
        <el-col v-for="card in page" :key="card.id"  :span="8">
          <div>
            <group-card :card="card" :status="getCardStatus()" :msg="this.msg"/>
          </div>
        </el-col> 
      </el-row>
    </el-scrollbar>
    <el-pagination
      :current-page="currentPage"
      :page-size=9
      :total="this.groupList.length"
      @current-change="handlePageChange"
    ></el-pagination>
  </div>
</template>
<script >
import { ElMessage, ElMessageBox } from 'element-plus'
import GroupCard from "../../Components/GroupCard.vue";
import axios from 'axios'

export default {
  data() {
    return {
      groupList: [], // 从后端获取的所有团体数据 
      currentPage: 1, // 当前页码
      input: "",
      keyword: "",
      status: "",
      msg: ""
    }
  },
  components: {
    GroupCard
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
    paginatedGroups() {
      if (this.groupList.length === 0) {
          return []; // 如果 groupList 是空数组，直接返回空数组
      }

      const pages = [];

      for(let i = 0; i < this.groupList.length; i += 9){
        pages.push(this.groupList.slice(i, i+9));
      }

      const currentPage = this.currentPage;
      const page = pages[currentPage - 1];
      const groups = [];

      for(let i = 0; i < page.length; i+=3){
        groups.push(page.slice(i,i+3));
      }

      return groups;
    },
    
  },
  methods: {
    getCardStatus() {
      // 示例：根据团队信息判断状态，返回对应状态码（0, 1, 2 等）
       return this.status;
    },
    handlePageChange(newPage) {
      // 当页码变化时更新当前页码
      this.currentPage = newPage;
    },
    // 从后端获取数据并更新groupList
    addNewGroup() {
      ElMessageBox.alert('This is a message', 'Title', {
        confirmButtonText: 'OK',
        // callback: (action: Action) => {
        //   ElMessage({
        //     type: 'info',
        //     message: `action: ${action}`,
        //   })
        // },
      })
    },
    search() {
            // axios({
            //     method: "GET",
            //     url: "http://127.0.0.1:8000/api/group/view",
            //     params: {
            //         keyword: this.keyword
            //     }
            // }).then((result) => {
            //         this.groupList = result.data.list   
            // });
    }
  },
}
</script>
  
<style scoped>
.searchTitle {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.searchBox {
    width: 240px;
}

.button-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>