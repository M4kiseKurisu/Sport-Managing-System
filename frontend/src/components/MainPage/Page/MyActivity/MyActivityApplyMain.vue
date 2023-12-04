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
    <router-view></router-view>
</template>

<script>
export default {
    data() {
        return {
            active: 0,
        }
    },
    methods: {
        newStep(data) {
            if (data.status) {
                if (this.active == 0) {
                    this.$router.push('/Page//MyActivity/Apply/Field');
                }
            }
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

.step {
    margin-top: 20px;
    margin-bottom: 30px;
    width: 50%;
    margin-left: 20%;
}
</style>