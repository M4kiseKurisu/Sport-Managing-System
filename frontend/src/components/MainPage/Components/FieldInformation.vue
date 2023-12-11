<template>
    <div class="all">
        <el-card :body-style="{ padding: '0px' }">
            <!-- <img class="image"
                src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" /> -->

            <div class="content">
                <div class="line">场地地址：{{ field.location }}</div>
                <div class="line">开放时间：{{ field.open_time }}</div>
                <div class="line">关闭时间：{{ field.close_time }}</div>
                <div class="button">
                    <el-button @click="dialogTableVisible = true" type="primary">
                        查看申请情况
                    </el-button>
                </div>



            </div>
        </el-card>

        <el-dialog v-model="dialogTableVisible" title="此场地借用情况">
            <div class="title">
                <div class="tip">选择日期：</div>
                <div class="tip">
                    <el-date-picker v-model="selectTime" type="date" placeholder="选择查看日期" format="YYYY-MM-DD"
                        value-format="YYYY-MM-DD" />
                </div>
                <div class="selectButton">
                    <el-button @click="search" type="primary"> 查询 </el-button>
                </div>
                <div class="selectButton">
                    <el-button @click="apply" type="primary"> 选择场地 </el-button>
                </div>
            </div>


            <el-table :data="timeTable" :stripe=true>
                <el-table-column property="start" label="开始时间" width="300px" />
                <el-table-column property="end" label="结束时间" />
            </el-table>
        </el-dialog>
    </div>
</template>

<script>
import axios from "axios"
import dayjs from 'dayjs'
export default {
    data() {
        return {
            dialogTableVisible: false,
            timeTable: [],
            selectTime: '',
        }
    },
    methods: {
        search() {
            if (this.selectTime === '') {
                this.$message({
                    showClose: true,
                    message: "未选择查询日期",
                    type: 'error'
                });
            }
            else {
                axios({
                    method: "GET",
                    url: "http://127.0.0.1:8000/api/field/usage",
                    params: {
                        fid: this.field.fid,
                        time: this.selectTime
                    },
                }).then((result) => {
                    if (result.data.status) {
                        console.log(this.field);
                        console.log(result.data);
                        this.timeTable = result.data.list;
                    }
                })
            }
        },
        apply() {
            console.log(this.field.fid);
            this.$emit("returnData", this.field.fid);
            this.$message({
                showClose: true,
                message: "成功选择场地！",
                type: 'success'
            });
        }
    },
    props: ["field"]  //field: fid, location, open_time, close_time
}
</script>

<style scoped>
.all {
    width: 90%;
    margin-left: 5%;
    ;
}

.image {
    width: 100%;
}

.content {
    margin-top: 15px;
    width: 80%;
    margin-left: 10%;
    margin-bottom: 10px;
    display: flex;
    justify-content: center;
    /* 水平方向居中对齐 */
    flex-direction: column;
}

.line {
    font-size: 16px;
    margin-bottom: 6px;
    display: flex;
    justify-content: center;
    /* 水平方向居中对齐 */
}

.button {
    margin-top: 6px;
    display: flex;
    justify-content: center;
    /* 水平方向居中对齐 */
}

.title {
    display: flex;
    align-items: center;
    margin-top: -15px;
}

.tip {
    font-size: 16px;
    margin-right: 12px;
}

.selectButton {
    margin-right: 10px;
}
</style>