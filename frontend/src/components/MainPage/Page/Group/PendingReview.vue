<template>
  <div>
  <el-table :data="filteredTableData" style="width: 80%">
    <el-table-column label="申请日期">
      <template #default="{ row }">
        {{ row.time }}
      </template>
    </el-table-column>
    <el-table-column label="申请对象">
      <template #default="{ row }">
        {{ row.group_name }}
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

<script lang="ts">
import { computed, ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  setup() {
    interface Application {
      time: string
      group_name: string
      status: string;
    }
    
    const groupList = ref<Application[]>([]);
    const small = ref(false)
    const background = ref(false)
    const disabled = ref(false)

    const search = ref('')
    const currentPage = ref(1);

    const totalPages = computed(() => {
      return Math.ceil(filteredTableData.value.length);
    });

    const filteredTableData = computed(() => {
      const start = (currentPage.value - 1) * 10;
      const end = start + 10;
      return filterTableData(groupList.value).slice(start, end);
    });

    const filterTableData = (data: Application[]) => {
      return data.filter(
        (item) =>
          !search.value ||
          item.time.includes(search.value) ||
          item.group_name.includes(search.value) ||
          item.status.includes(search.value)
      );
    };

    const handleCurrentChange = (val: number) => {
      console.log(`current page: ${val}`)
    }

    const handleApplication = (op: number) => {
  
    }

    onMounted(() => {
      const storedUid = sessionStorage.getItem('uid');
      if (storedUid) {
        const uid = JSON.parse(storedUid);
        axios({
          method: "GET",
          url: "http://127.0.0.1:8000/api/group/apply",
          params: {
            uid: uid,
            method: "accept"
          }
        }).then((result) => {
          groupList.value = result.data.list;
          // Process any other data as needed from the result
        }).catch((error) => {
          console.error('Error fetching group data:', error);
        });
      } else {
        console.error('UID not found in sessionStorage');
      }
    });

    return {
      small,
      background,
      disabled,
      search,
      currentPage,
      totalPages,
      filteredTableData,
      handleCurrentChange,
      handleApplication
    };
  }
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
