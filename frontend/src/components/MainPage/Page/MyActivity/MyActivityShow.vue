<template>
    <div class="title">
        <div>我的活动</div>
    </div>
    <div>
        <el-row v-for="(group, index) in groups" :gutter="20" :key="index">
            <el-col v-for="item in group" :key="item.aid" :span="8">
                <Card :name="item.name" :start_time="item.start_time" :end_time="item.end_time" :category="item.category"
                    :capacity="item.capacity" :maximum="item.maximum" :favor="item.favor" :is_favor="item.is_favor"
                    :aid="item.aid" />
            </el-col>
        </el-row>
    </div>

    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="this.list.length" @current-change="handlePageChange" />
    </div>
</template>

<script>
import axios from "axios"
import Card from "../../Components/MyActivityShowCard.vue"
export default {
    data() {
        return {
            list: [],
            current_page: 1,
        }
    },
    methods: {
        handlePageChange(pageNo) {
            this.current_page = pageNo;
        }
    },
    created() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/user/activity/view",
            params: {
                uid: JSON.parse(sessionStorage.getItem("uid")),
            }
        }).then((result) => {
            if (result.data.status) {
                this.list = result.data.list;
            }
        })
    },
    components: {
        Card,
    },
    computed: {
        groups() {
            let groups = [];
            for (let i = (this.current_page - 1) * 12; i < this.current_page * 12; i += 3) {
                groups.push(this.list.slice(i, i + 3))
            }
            return groups;
        }
    }
}
</script>

<style>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.pagination {
    display: flex;
    justify-content: flex-end;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-right: 30px;
}
</style>