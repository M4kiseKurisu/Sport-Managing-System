<template>
    <div class="title">
        <div>团体借出</div>
    </div>

    <BorrowFormRow :isTitle=true :isGroup=true />
    <BorrowFormRow v-if="have1" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have2" :information="information2" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have3" :information="information3" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have4" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have5" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have6" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have7" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have8" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have9" :information="information1" :isTitle=false :isGroup=true />
    <BorrowFormRow v-if="have10" :information="information1" :isTitle=false :isGroup=true />

    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="1000" @current-change="handlePageChange" />
    </div>
</template>

<script>
import BorrowFormRow from "../../Components/BorrowFormRow.vue"
export default {
    data() {
        return {
            have1: true,
            have2: true,
            have3: true,
            have4: false,
            have5: false,
            have6: false,
            have7: false,
            have8: false,
            have9: false,
            have10: false,


            information1: {
                name: "篮球",
                amount: "2",
                returnTime: "2023/11/20",
                group: "fyb郭楠培养中心",
                state: "未归还",
            },
            information2: {
                name: "篮球",
                amount: "1",
                returnTime: "2023/9/7",
                group: "fyb郭楠培养中心",
                state: "已归还",
            },
            information3: {
                name: "篮球",
                amount: "8",
                returnTime: "2023/9/5",
                group: "fyb郭楠培养中心",
                state: "已归还",
            }
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
        },
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