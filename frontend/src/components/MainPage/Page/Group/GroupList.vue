<template>
<div class="button-row">
  <el-button text @click="addNewGroup">Create Group</el-button>
  <div class="searchTitle">
    <div class="searchBox">
      <el-input v-model="keyword" placeholder="输入查询团体名"></el-input>
    </div>
    <el-button @click="search">查 询</el-button>
  </div>
</div>

<div>
    <el-scrollbar class="scrollbar" max-height="100%">
      <el-row>
        <el-col v-for="(page, index) in paginatedGroups" :key="index" :span="8">
          <div v-for="card in page" :key="card.id">
            <!-- 在这里创建卡片并展示每个团队的信息 -->
            <el-card>
              <div>{{ card.name }}</div>
              <!-- 其他团队信息... -->
            </el-card>
          </div>
        </el-col>
      </el-row>
    </el-scrollbar>
    <el-pagination
      :current-page="currentPage"
      :page-size="pageSize"
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
      pageSize: 9, // 每页显示的团队数量
      currentPage: 1, // 当前页码
      input: "",
      keyword: "",
    }
  },
  components: {
    GroupCard
  },
  computed: {
    paginatedGroups() {
      // 根据当前页和每页显示的数量切分数据
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.groupList.slice(startIndex, endIndex);
    },
  },
  methods: {
    handlePageChange(newPage) {
      // 当页码变化时更新当前页码
      this.currentPage = newPage;
    },
    // 从后端获取数据并更新groupList
    fetchDataFromBackend() {
      // 发送请求到后端获取所有团体数据，然后更新groupList
      // 示例：axios.get('/api/groups').then(response => { this.groupList = response.data; });
    },
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
                url: "http://127.0.0.1:8000/api/equipment/view",
                params: {
                    keyword: this.keyword
                }
            }).then((result) => {
                if (result.data.status) {
                    this.list = result.data.list
                }
            });
    }
  },
  created() {
    // 页面创建时从后端获取数据
    this.fetchDataFromBackend();
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