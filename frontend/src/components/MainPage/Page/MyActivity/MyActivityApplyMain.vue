<template>
    <div class="title">
        <div>申请活动</div>
    </div>
    <div class="step">
        <el-steps :active="active" finish-status="success">
            <el-step title="填写基本信息" />
            <el-step title="选择场地" />
            <el-step title="确认申请" />
        </el-steps>
    </div>

    <div>
        <Apply v-if="this.active == 0" @returnData="newStep" />
        <Field v-else-if="this.active == 1" @returnData="newStep_2" />
        <Result v-else :isSuccess="this.success" :msg="this.message" />
    </div>
</template>

<script>
import axios from 'axios'
import Apply from "./MyActivityApply.vue"
import Field from "./MyActivitySelectField.vue"
import Result from "./MyActivityResultShow.vue"
export default {
    data() {
        return {
            active: 0,
            information1: '',
            information2: '',
            success: '',
            message: '',
        }
    },
    methods: {
        newStep(data) {
            if (data.status) {
                if (this.active == 0) {
                    this.active++;
                    this.information1 = data.information;
                }
                this.$message({
                    showClose: true,
                    message: data.msg,
                    type: 'success'
                });
            }

            else {
                this.$message({
                    showClose: true,
                    message: data.msg,
                    type: 'error'
                });
            }
        },
        newStep_2(data) {
            this.information2 = data;
            this.applyActivity();
            this.active++;
        },
        applyActivity() {
            if (this.information1 === '' || this.information2 === '') {
                return;
            }

            let inputData = new FormData();

            console.log(this.information1.type);
            console.log(this.information1.gid);

            inputData.append("uid", JSON.parse(sessionStorage.getItem("uid")));
            inputData.append("type", this.information1.type);
            if (this.information1.type === "1") {
                inputData.append("gid", this.information1.gid);
            }
            inputData.append("name", this.information1.name);
            inputData.append("desc", this.information1.desc);
            inputData.append("fid", this.information2.fid);
            inputData.append("category", this.information1.category);
            inputData.append("tags", this.information1.tags);
            inputData.append("maximum", this.information1.maximum);
            inputData.append("start_time", this.information2.start_time);
            inputData.append("end_time", this.information2.end_time);
            inputData.append("private", this.information1.private);
            inputData.append("picture", this.information1.picture);

            console.log(inputData);

            axios({
                method: "POST",
                url: "http://127.0.0.1:8000/api/activity/create",
                data: inputData
            }).then((result) => {
                console.log(result);
                if (result.data.status) {
                    this.success = true;
                    this.message = result.data.msg;
                }
                else {
                    this.success = false;
                    this.message = result.data.msg;
                }
            })
        }
    },
    components: {
        Apply,
        Field,
        Result,
    },
    created() {
        this.active = 0;
    }
}
</script>

<style>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.step {
    margin-top: 20px;
    margin-bottom: 30px;
    width: 50%;
    margin-left: 20%;
}
</style>