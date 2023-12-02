<template>
    <div>
        <el-table :data="filteredTableData" style="width: 100%">
            <el-table-column label="申请日期">
                <template #default="{ row }">
                    {{ row.time }}
                </template>
            </el-table-column>
            <el-table-column label="申请对象">
                <template #default="{ row }">
                    {{ row.user_name }}
                </template>
            </el-table-column>
            <el-table-column label="申请状态">
                <template #default="{ row }">
                    {{ row.status }}
                </template>
            </el-table-column>
        </el-table>

        <el-pagination :small="small" :disabled="disabled" :background="background" layout="prev, pager, next"
            :page-size="10" :total="totalPages" v-model:current-page="currentPage" @current-change="handleCurrentChange" />
    </div>
</template>

<script lang="ts">
import { computed, ref, onMounted } from "vue";
import axios from "axios";

export default {
    setup() {
        interface Application {
            time: string;
            user_name: string;
            status: string;
        }
        const small = ref(false);
        const background = ref(false);
        const disabled = ref(false);

        const currentPage = ref(1);
        const search = ref("");
        const friendList = ref<Application[]>([]); // 替换 Application 类型为实际的类型

        const totalPages = computed(() => {
            return Math.ceil(filteredTableData.value.length);
        });

        const filteredTableData = computed(() => {
            const start = (currentPage.value - 1) * 10;
            const end = start + 10;
            return filterTableData(friendList.value).slice(start, end);
        });

        const filterTableData = (data: Application[]) => {
            return data.filter(
                (item) =>
                    !search.value ||
                    item.time.includes(search.value) ||
                    item.user_name.includes(search.value) ||
                    item.status.includes(search.value)
            );
        };

        const handleCurrentChange = (val: number) => {
            console.log(`current page: ${val}`);
        };

        onMounted(() => {
            const storedUid = sessionStorage.getItem("uid");
            if (storedUid) {
                const uid = JSON.parse(storedUid);
                axios({
                    method: "GET",
                    url: "http://127.0.0.1:8000/api/friend/apply",
                    params: {
                        uid: uid,
                        method: "send",
                    },
                })
                    .then((result) => {
                        friendList.value = result.data.list;
                        // Process any other data as needed from the result
                    })
                    .catch((error) => {
                        console.error("Error fetching friend data:", error);
                    });
            } else {
                console.error("UID not found in sessionStorage");
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
        };
    },
};
</script>

<style scoped>
/* Your styles */
</style>
