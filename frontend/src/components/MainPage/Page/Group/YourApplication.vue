<template>
  <div>
  <el-table :data="filteredTableData" style="width: 100%">
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
    <el-table-column label="申请状态">
      <template #default="{ row }">
        {{ row.status }}
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

<script lang="ts">
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

]

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