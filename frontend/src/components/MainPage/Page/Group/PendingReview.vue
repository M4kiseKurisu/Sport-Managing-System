<template>
  <div>
  <el-table :data="filteredTableData" style="width: 80%">
    <el-table-column label="申请日期">
      <template #default="{ row }">
        {{ row.data }}
      </template>
    </el-table-column>
    <el-table-column label="申请对象">
      <template #default="{ row }">
        {{ row.group }}
      </template>
    </el-table-column>
    <el-table-column label="审核">
      <template #default="scope">
        <el-button
          size="small"
          type="success"
          @click="handleApplication(1)"
          >同意</el-button
        >
        <el-button
          size="small"
          type="danger"
          @click="handleApplication(2)"
          >拒绝</el-button
        >
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

interface Application {
  data: string
  group: string
  status: string;
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
      data.data.includes(search.value)
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

const tableData: Application[] = [
  {
    data: '2023-11-18',
    group: 'group1',
    status:'审核中'
  },
  {
    data: '2023-11-18',
    group: 'group2',
    status:'审核中'
  },
  {
    data: '2023-11-18',
    group: 'group3',
    status:'审核通过'
  },
  {
    data: '2023-11-18',
    group: 'group4',
    status:'拒绝'
  },
  {
    data: '2023-11-18',
    group: 'group5',
    status:'审核中'
  },
  {
    data: '2023-11-18',
    group: 'group6',
    status:'审核中'
  },
  {
    data: '2023-11-18',
    group: 'group7',
    status:'审核通过'
  },
  {
    data: '2023-11-18',
    group: 'group8',
    status:'拒绝'
  },
  {
    data: '2023-11-18',
    group: 'group9',
    status:'审核中'
  },
  {
    data: '2023-11-18',
    group: 'group10',
    status:'审核中'
  },
  {
    data: '2023-11-18',
    group: 'group11',
    status:'审核通过'
  },
  {
    data: '2023-11-18',
    group: 'group12',
    status:'拒绝'
  },

]

const handleApplication = (op: number) => {
  
}
</script>

<style scoped>
.Application-info {
  display: flex;
  align-items: center;
}

  group {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}
</style>
