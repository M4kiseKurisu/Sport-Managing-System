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
            <group-card :card="card" :status="getCardStatus(card)" />
          </div>
        </el-col> 
      </el-row>
    </el-scrollbar>
    <el-pagination
      :current-page="currentPage"
      :page-size=9
      :total="groupList.length"
      @current-change="handlePageChange"
    ></el-pagination>
  </div>
</template>
<script lang="ts">
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'
import GroupCard from "../../Components/GroupCard.vue";
import axios from 'axios'

export default {
  data() {
    return {
      groupList: [], // 从后端获取的所有团体数据 
      currentPage: 1, // 当前页码
      input: "",
      keyword: "",
    }
  },
  components: {
    GroupCard
  },
  created() {
    axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/group/view"
        }).then((result) => {
            if (result.data.status) {
                this.groupList = result.data.list
            }
    });
  },
  computed: {
    cutPage() {
      const pageSize = 9;
      const pages = [];
      
      for(let i = 0; i < this.groupList.length; i += 9){
        pages.push(this.groupList.slice(i, i+9));
      }
      return pages;
    },

    paginatedGroups() {
      const currentPage = this.currentPage;
      const page = this.cutPage[currentPage - 1];
      const groups = [];

      for(let i = 0; i < page.length; i+=3){
        groups.push(page.slice(i,i+3));
      }

      return groups;
    },
    
  },
  methods: {
    getCardStatus(card) {
      // 示例：根据团队信息判断状态，返回对应状态码（0, 1, 2 等）
       return 0;
    },
    handlePageChange(newPage) {
      // 当页码变化时更新当前页码
      this.currentPage = newPage;
    },
    // 从后端获取数据并更新groupList
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
    },
    search() {
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/group/view",
                params: {
                    keyword: this.keyword
                }
            }).then((result) => {
                    this.groupList = result.data.list   
            });
    }
  },

}
</script>
  
<style scoped>
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

.searchTitle {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.searchTip {
    font-size: 16px;
    margin-right: 20px;
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