<template>
    <div class="search">

        <div v-if="isGroup" class="selecter">
            <div>团体：</div>
            <div>
                <el-input v-model="groupKeyword" placeholder="团体关键字"></el-input>
            </div>

        </div>

        <div class="selecter">
            <div>器材类型：</div>
            <div class="select">
                <el-select v-model="value1" placeholder="器材类型">
                    <el-option v-for="item in options" :key="item.eid" :label="item.category" :value="item.category" />
                </el-select>
            </div>

        </div>

        <div class="selecter">
            <div>借用时间：</div>
            <el-date-picker v-model="date" type="date" placeholder="选择日期" value-format="YYYY-MM-DD" />
        </div>

        <div class="selecter">
            <div>归还情况：</div>
            <div class="select">
                <el-select v-model="value2" placeholder="归还情况">
                    <el-option v-for="item in state" :key="item.value" :label="item.nowState" :value="item.value" />
                </el-select>
            </div>

        </div>

        <div class="selecter">
            <el-button type="primary" plain @click="search()">查询记录</el-button>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            groupKeyword: '',
            value1: '',
            value2: '',
            options: [],
            state: [
                {
                    value: 0,
                    nowState: "未归还"
                },
                {
                    value: 2,
                    nowState: "已归还"
                }
            ],
            date: '',
        }
    },
    methods: {
        search() {
            let data = {
                group: this.groupKeyword,
                type: this.value1,
                time: this.date,
                state: this.value2
            }
            console.log(data);
            this.$emit("someEvent", data);
        }
    },
    created() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/equipment/view"
        }).then((result) => {
            if (result.data.status) {
                this.options = result.data.list;
            }
        })
    },
    props: ["isGroup"]
}
</script>

<style scoped>
.search {
    display: flex;
}

.selecter {
    display: flex;
    margin-left: 16px;
    align-items: center;
}

.select {
    width: 140px;
}
</style>