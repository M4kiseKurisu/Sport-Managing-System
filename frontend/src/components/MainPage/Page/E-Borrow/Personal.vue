<template>
    <div class="title">
        <div>个人借出</div>
    </div>

    <BorrowFormRow :isTitle=true :isGroup=false />
    <!-- <BorrowFormRow v-if="have1" :information="list[0]" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have2" :information="information2" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have3" :information="information3" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have4" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have5" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have6" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have7" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have8" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have9" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have10" :information="information1" :isTitle=false :isGroup=false /> -->
    <BorrowFormRow v-for="(item, i) in groups" :information="item" :isTitle=false :isGroup=false />
    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="this.list.length" @current-change="handlePageChange" />
    </div>
</template>

<script>
import BorrowFormRow from "../../Components/BorrowFormRow.vue"
import axios from 'axios'
export default {
    data() {
        return {
            current_page: 1,

            // have1: false,
            // have2: false,
            // have3: false,
            // have4: false,
            // have5: false,
            // have6: false,
            // have7: false,
            // have8: false,
            // have9: false,
            // have10: false,


            // information1: {
            //     name: "篮球",
            //     amount: "2",
            //     returnTime: "2023/11/20",
            //     state: "未归还",
            // },
            // information2: {
            //     name: "篮球",
            //     amount: "1",
            //     returnTime: "2023/9/7",
            //     state: "已归还",
            // },
            // information3: {
            //     name: "篮球",
            //     amount: "8",
            //     returnTime: "2023/9/5",
            //     state: "已归还",
            // },

            list: [],
            // information: {
            //     name: list[0].category,
            //     amount: list[0].lend_amount,
            //     returnTime: list[0].end_time,
            //     state: list[0].is_return,
            // }
        }
    },
    components: {
        BorrowFormRow,
    },
    methods: {
        handlePageChange(pageNo) {
            // pageNo 是你点击的页号
            // 在这里，你可以获取该页面的数据，并更新你的组件
            // 确保你的请求是异步的，以避免阻塞用户界面
            this.current_page = pageNo;
        }
    },
    created() {
        console.log(JSON.parse(sessionStorage.getItem('uid')));
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/equipment/record",
            params: {
                uid: JSON.parse(sessionStorage.getItem('uid'))
            }
        }).then((result) => {
            if (result.data.status) {
                for (let i = 0; i < result.data.list.length; i++) {
                    this.list.push({
                        url: 'http://127.0.0.1:8000' + result.data.list[i].pic,
                        name: result.data.list[i].category,
                        amount: String(result.data.list[i].lend_amount),
                        returnTime: result.data.list[i].end_time,
                        state: result.data.list[i].is_return,
                    });
                }
            }
        });
    },
    computed: {
        groups() {
            let end = (this.list.length < 10 * this.current_page) ? this.list.length : 10 * this.current_page;
            return this.list.slice(10 * (this.current_page - 1), end);
        }
    }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 30px;
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