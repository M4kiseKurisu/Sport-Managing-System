<template>
  <div>
  <el-table :data="filteredTableData" style="width: 80%">
    <el-table-column label="呢称" width="200">
      <template #default="scope">
        <div class="user-info">
          <img :src="getAvatar(scope.row)" alt="avatar" class="avatar">
          <span>{{ scope.row.name }}</span>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="个性签名">
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
          @click="handleDelete(scope.$index, scope.row)"
          >Delete</el-button>
      </template>
    </el-table-column>
  </el-table>

  <el-pagination
  :small="small"
  :disabled="disabled"
  :background="background"
  layout="prev, pager, next"
  :page-size="10"
  :total="totalPages"
  v-model:current-page="currentPage"
  @current-change="handleCurrentChange"
    />
  </div>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'

interface User {
  name: string
  avatar: string
  description: string;
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
  const start = (currentPage.value - 1) * 10;
  const end = start + 10;
  return filterTableData.value.slice(start, end);
});

const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
}

const handleDelete = (index: number, row: User) => {
  console.log(index, row)
}

const tableData: User[] = [
  {
    name: 'Tom',
    avatar: './src/images/emptyAvatar.png',
    description:'这个人很懒，还没有编写签名'
  },
  {
    name: 'John',
    avatar: './src/images/emptyAvatar.png',
    description:'这个人很懒，还没有编写签名'
  },
  {
    name: 'Morgan',
    avatar: './src/images/emptyAvatar.png',
    description:'这个人很懒，还没有编写签名'
  },
  {
    name: 'Jessy',
    avatar: './src/images/emptyAvatar.png',
    description:'这个人很懒，还没有编写签名'
  },

]

const getAvatar = (user: User) => user.avatar
</script>

<style scoped>
.user-info {
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
