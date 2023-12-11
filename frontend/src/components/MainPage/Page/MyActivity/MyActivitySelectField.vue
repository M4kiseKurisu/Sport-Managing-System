<template>
    <div class="formItem">
        <div class="formTip">选择日期：</div>
        <div class="formInput">
            <el-date-picker v-model="date" type="date" placeholder="选择活动日期" format="YYYY/MM/DD" value-format="YYYY-MM-DD"
                @change="updateDatePicker" />
        </div>
    </div>

    <div class="formItem">
        <div class="formTip">开始时间：</div>
        <div class="formInput">
            <el-time-picker v-model="startTime" placeholder="选择开始时间" format="HH:mm:ss" value-format="HH:mm:ss" />
        </div>
        <div class="formTip">结束时间：</div>
        <div class="formInput">
            <el-time-picker v-model="endTime" placeholder="选择结束时间" format="HH:mm:ss" value-format="HH:mm:ss" />
        </div>
    </div>

    <div class="formItem">
        <div class="formTip">场地类型：</div>
        <div class="formInput">
            <el-select v-model="fieldType" placeholder="选择场地类型">
                <el-option v-for="item in fieldTypes" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
        </div>
        <div class="formTip">
            <el-button type="primary" plain @click="searchField">查询场地</el-button>
        </div>

        <div class="formTip">
            <el-button type="primary" @click="commit">确认申请</el-button>
        </div>
    </div>

    <div class="showField">
        <el-row v-for="(group, index) in groups" :gutter="20" :key="index">
            <el-col v-for="item in group" :key="item.fid" :span="6">
                <field :field="item" @returnData="returnField" />
            </el-col>
        </el-row>
    </div>
</template>

<script>
import axios from 'axios'
import field from '../../Components/FieldInformation.vue'
import dayjs from 'dayjs'
export default {
    data() {
        return {
            fieldType: '',
            fieldTypes: [],
            fieldList: [],
            date: '',
            startTime: '',
            endTime: '',
            selectFid: '',
        }
    },
    methods: {
        searchField() {
            if (this.fieldType != '') {
                axios({
                    method: "GET",
                    url: "http://127.0.0.1:8000/api/field/view",
                    params: {
                        category: this.fieldType
                    }
                }).then((result) => {
                    if (result.data.status) {
                        this.fieldList = result.data.list;
                        console.log(this.groups);
                    }
                })
                console.log(this.fieldList);
            }
        },
        returnField(data) {
            this.selectFid = data;
        },
        commit() {
            if (this.date === '' || this.startTime === '' || this.endTime === '') {
                console.log(1);
                this.$message({
                    showClose: true,
                    message: "未完整选择活动时间",
                    type: 'error'
                });
            }
            else if (this.date < dayjs().format('YYYY-MM-DD') || (this.date == dayjs().format('YYYY-MM-DD') && this.startTime < dayjs().format('HH:mm:ss'))) {
                console.log(2);
                this.$message({
                    showClose: true,
                    message: "开始时间必须晚于当前时间！",
                    type: 'error'
                });
            }

            else if (this.startTime > this.endTime) {
                console.log(3);
                this.$message({
                    showClose: true,
                    message: "开始时间必须早于结束时间！",
                    type: 'error'
                });
            }

            else if (this.selectFid === '') {
                console.log(4);
                this.$message({
                    showClose: true,
                    message: "未申请场地！",
                    type: 'error'
                });
            }

            else {
                console.log(5);
                this.$message({
                    showClose: true,
                    message: "成功申请！",
                    type: 'success'
                });
                let start = this.date + " " + this.startTime;
                let end = this.date + " " + this.endTime;
                this.$emit("returnData", {
                    start_time: start,
                    end_time: end,
                    fid: this.selectFid
                });
            }
        }
    },
    created() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/field/view",
            params: {
                category: ''
            }
        }).then((result) => {
            if (result.data.status) {
                this.fieldTypes = [];
                for (let i = 0; i < result.data.list.length; i++) {
                    this.fieldTypes.push({
                        value: result.data.list[i],
                        label: result.data.list[i],
                    })
                }
            }
        })
    },
    components: {
        field,
    },
    computed: {
        groups() {
            let groups = [];
            for (let i = 0; i < this.fieldList.length; i += 4) {
                groups.push(this.fieldList.slice(i, i + 4));
            }
            return groups;
        }
    }
}
</script>

<style scoped>
.formItem {
    display: flex;
    align-items: center;
    margin-top: 10px;
    margin-bottom: 10px;
}

.formTip {
    font-size: 16px;
    margin-right: 12px;
}

.formInput {
    margin-right: 24px;
}

.showField {
    margin-top: 30px;
}
</style>