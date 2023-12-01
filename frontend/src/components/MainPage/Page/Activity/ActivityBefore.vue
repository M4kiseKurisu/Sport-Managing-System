<template>
    <!-- 界面标题 -->
    <div class="title">
        <div>过往活动</div>
    </div>

    <!-- 表项 -->
    <div class="form">
        <BeforeActivityRow v-for="(item, index) in groups" :key="index" :information="item" />
    </div>

    <!-- 换页器 -->
    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="this.list.length" @current-change="handlePageChange" />
    </div>
</template>

<script>
import axios from 'axios'
import BeforeActivityRow from '../../Components/BeforeActivityRow.vue';
export default {
    data() {
        return {
            current_page: 1,
            list: [],
        };
    },
    methods: {
        draw() {
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/activity/view/inactive",
                params: {
                    uid: JSON.parse(sessionStorage.getItem("uid")),
                    type: 2,
                    method: "time"
                }
            }).then((result) => {
                if (result.data.status) {
                    this.list = result.data.list;
                }
            });
        },
        handlePageChange(pageNo) {
            this.current_page = pageNo;
        }
    },
    created() {
        this.draw()
    },
    components: { BeforeActivityRow },
    computed: {
        groups() {
            let end = this.list.length < 6 * this.current_page ? this.list.length : 6 * this.current_page;
            return this.list.slice(6 * (this.current_page - 1), end);
        }
    }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.row {
    width: 60%;
    height: 200px;
}

.form {
    margin-top: 20px;
}

.pagination {
    display: flex;
    justify-content: flex-end;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-right: 7%;
}
</style>