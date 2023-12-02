<template>
    <div>
        <el-table :data="filteredTableData" style="width: 80%">

            <el-table-column label="申请日期">
                <template #default="{ row }">
                    {{ row.time }}
                </template>
            </el-table-column>

            <el-table-column label="申请人">
                <template #default="{ row }">
                    {{ row.user_name }}
                </template>
            </el-table-column>

            <el-table-column label="申请信息">
                <template #default="{ row }">
                    <div v-if="row.content.length > 10">
                        <el-collapse>
                            <el-collapse-item title="点击展开" v-if="row.content.length > 10">
                                {{ row.content }}
                            </el-collapse-item>
                        </el-collapse>
                    </div>
                    <div v-else>
                        {{ row.content }}
                    </div>
                </template>
            </el-table-column>

            <el-table-column label="审核">
                <template #default="scope">
                    <div v-if="scope.row.status === '申请中'">
                        <el-button size="small" type="success" @click="handleApplication(scope.row, 1)">同意</el-button>
                        <el-button size="small" type="danger" @click="handleApplication(scope.row, 2)">拒绝</el-button>
                    </div>
                    <div v-else>
                        <span>{{ scope.row.status }}</span>
                    </div>
                </template>
            </el-table-column>
        </el-table>

        <el-pagination :small="small" :disabled="disabled" :background="background" layout="prev, pager, next"
            :page-size="10" :total="totalPages" v-model:current-page="currentPage" @current-change="handleCurrentChange" />
    </div>
</template>

<script lang="ts">
import { computed, ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import axios from 'axios'

export default {
    setup() {
        interface Application {
            uid: number
            user_name: string
            time: string
            status: string
            content: string
        }

        const friendList = ref<Application[]>([]);
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
            return filterTableData(friendList.value).slice(start, end);
        });

        const filterTableData = (data: Application[]) => {
            return data.filter(
                (item) =>
                    !search.value ||
                    item.time.includes(search.value) ||
                    item.status.includes(search.value)
            );
        };

        const handleCurrentChange = (val: number) => {
            console.log(`current page: ${val}`)
        }

        const handleApplication = (row, op: number) => {
            let res = false;
            if (op == 1) {
                res = true;
            }
            axios({
                method: "POST",
                url: "http://127.0.0.1:8000/api/friend/apply",
                data: {
                    receiver: sessionStorage.getItem('uid'),
                    sender: row.uid,
                    res: res
                }
            }).then(response => {
                const { status, msg } = response.data;
                if (status === true) {
                    ElMessage({
                        type: 'success',
                        message: msg,
                    });
                    const storedUid = sessionStorage.getItem('uid');
                    if (storedUid) {
                        const uid = JSON.parse(storedUid);
                        axios({
                            method: "GET",
                            url: "http://127.0.0.1:8000/api/friend/apply",
                            params: {
                                uid: uid,
                                method: "accept"
                            }
                        }).then((result) => {
                            friendList.value = result.data.list;
                            console.log(friendList)
                        })
                    }
                } else {
                    ElMessage({
                        type: 'error',
                        message: msg,
                    });
                }
            }).catch(error => {
                console.error(error);
            });
        }

        onMounted(() => {
            const storedUid = sessionStorage.getItem('uid');
            if (storedUid) {
                const uid = JSON.parse(storedUid);
                axios({
                    method: "GET",
                    url: "http://127.0.0.1:8000/api/friend/apply",
                    params: {
                        uid: uid,
                        method: "accept"
                    }
                }).then((result) => {
                    console.log(result.data)
                    friendList.value = result.data.list;
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
