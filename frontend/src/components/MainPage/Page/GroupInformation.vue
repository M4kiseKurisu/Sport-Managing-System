<template>
 <h1 style="text-align: center; font-size: 24px;">你的团体</h1>

    <el-scrollbar class="scrollbar" max-height="180px">
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
                <el-button text class="button">查看详情</el-button>
                <el-button text class="button">退出</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-scrollbar>
  <div class="groupList">
  <h1 style="text-align: center; font-size: 24px;">团体列表</h1>
  <el-button @click="addNewGroup">Create Group</el-button>
  <div>
  <el-table :data="filteredTableData" style="width: 100%">
    <el-table-column label="Name" width="200">
      <template #default="scope">
        <div class="group-info">
          <img :src="getAvatar(scope.row)" alt="avatar" class="avatar">
          <span>{{ scope.row.name }}</span>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="Description">
      <template #default="{ row }">
        {{ row.description }}
      </template>
    </el-table-column>
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" size="small" placeholder="Type to search" />
      </template>
      <template #default="scope">
        <el-button
          size="small"
          type="danger"
          @click="handleJoin()"
          >加入</el-button
        >
      </template>
    </el-table-column>

  </el-table>

  <el-pagination
  :small="small"
  :disabled="disabled"
  :background="background"
  layout="prev, pager, next"
  :page-size="6"
  :total="totalPages"
  v-model:current-page="currentPage"
  @current-change="handleCurrentChange"
    />
  </div>
  </div>
  </template>


  <script lang="ts" setup>
  import { ref, computed } from 'vue';

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


const small = ref(false)
const background = ref(false)
const disabled = ref(false)

const search = ref('')
const currentPage = ref(1);
const totalPages = computed(() => {
  console.log(Math.ceil(filterTableData.value.length ))
  return Math.ceil(filterTableData.value.length );
});
const filterTableData = computed(() =>
  tableData.filter(
    (data) =>
      !search.value ||
      data.name.includes(search.value)
  )
)
const filteredTableData = computed(() => {
  const start = (currentPage.value - 1) * 6;
  const end = start + 6;
  return filterTableData.value.slice(start, end);
});

const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
}

const handleJoin = () => {
  
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

const addNewGroup = () => {
    tableData.push({
      name: `group${tableData.length + 1}`,
      avatar: './src/images/group-default-picture.png',
      description: '寻找志同道合的伙伴~',
    });
    console.log(tableData)
  };


const getAvatar = (group: Groups) => group.avatar

  </script>
  
<style scoped>
.groupList {
  margin-top: -90px; /* 使用负外边距向上移动 */
}

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

  .group-info {
  display: flex;
  align-items: center;
 }

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}
  
  </style>
  